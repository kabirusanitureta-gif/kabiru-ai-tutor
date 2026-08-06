import React, { useEffect, useState } from "react";
import Layout from "../components/Layout.jsx";
import { useAuth } from "../context/AuthContext.jsx";
import {
  getDashboardStats, listAdminUsers, changeUserRole, toggleUserActive,
  softDeleteUser, restoreUser, listRoles, listPermissionsCatalog, setRolePermission,
  getAuditLogs,
} from "../api/endpoints.js";

const ROLE_LABELS = {
  super_admin: "Super Admin",
  admin: "Admin",
  moderator: "Moderator",
  teacher: "Teacher",
  student: "Student",
};

function StatCard({ label, value }) {
  return (
    <div className="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-4">
      <div className="text-2xl font-bold">{value ?? "—"}</div>
      <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">{label}</div>
    </div>
  );
}

export default function Admin() {
  const { user } = useAuth();
  const isSuperAdmin = user?.role === "super_admin";

  const [tab, setTab] = useState("overview");
  const [stats, setStats] = useState(null);
  const [users, setUsers] = useState([]);
  const [roles, setRoles] = useState([]);
  const [permCatalog, setPermCatalog] = useState({ permissions: [], roles: [] });
  const [auditLogs, setAuditLogs] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const loadOverview = () => getDashboardStats().then((r) => setStats(r.data));
  const loadUsers = () => listAdminUsers().then((r) => setUsers(r.data));
  const loadRoles = () =>
    Promise.all([listRoles(), listPermissionsCatalog()]).then(([r1, r2]) => {
      setRoles(r1.data);
      setPermCatalog(r2.data);
    });
  const loadAuditLogs = () => getAuditLogs({ limit: 50 }).then((r) => setAuditLogs(r.data));

  useEffect(() => {
    setError("");
    setLoading(true);
    const loader =
      tab === "overview" ? loadOverview :
      tab === "users" ? loadUsers :
      tab === "roles" ? loadRoles :
      loadAuditLogs;
    loader().catch((err) => setError(err?.response?.data?.detail || "Could not load data.")).finally(() => setLoading(false));
  }, [tab]);

  const handleRoleChange = async (userId, newRole) => {
    try {
      await changeUserRole(userId, newRole);
      loadUsers();
    } catch (err) {
      setError(err?.response?.data?.detail || "Could not change role.");
    }
  };

  const handleToggleActive = async (userId) => {
    await toggleUserActive(userId);
    loadUsers();
  };

  const handleSoftDelete = async (userId) => {
    if (!window.confirm("Soft-delete this user? Their data is kept but they can no longer log in.")) return;
    await softDeleteUser(userId);
    loadUsers();
  };

  const handleRestore = async (userId) => {
    await restoreUser(userId);
    loadUsers();
  };

  const handlePermToggle = async (role, permission, currentlyAllowed) => {
    try {
      await setRolePermission(role, permission, !currentlyAllowed);
      loadRoles();
    } catch (err) {
      setError(err?.response?.data?.detail || "Only Super Admin can edit permissions.");
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-1">Admin Dashboard</h1>
      <p className="text-sm text-slate-500 dark:text-slate-400 mb-5">
        Signed in as {ROLE_LABELS[user?.role] || user?.role}
      </p>

      <div className="flex gap-2 mb-5 overflow-x-auto">
        {["overview", "users", "roles", "audit"].map((t) => (
          <button
            key={t}
            onClick={() => setTab(t)}
            className={`px-4 py-2 rounded-xl text-sm font-medium whitespace-nowrap ${
              tab === t ? "bg-brand-600 text-white" : "bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700"
            }`}
          >
            {t === "overview" ? "Overview" : t === "users" ? "Users & Roles" : t === "roles" ? "Permissions" : "Audit Log"}
          </button>
        ))}
      </div>

      {error && (
        <div className="mb-4 p-3 rounded-xl bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 text-sm">
          {error}
        </div>
      )}

      {loading && <div className="text-sm text-slate-500">Loading…</div>}

      {!loading && tab === "overview" && stats && (
        <div className="space-y-6">
          <div>
            <h2 className="font-semibold mb-2">Users</h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
              <StatCard label="Total users" value={stats.users.total} />
              <StatCard label="Active users" value={stats.users.active} />
              <StatCard label="Chatted (last 5 min)" value={stats.users.online_last_5min} />
              <StatCard label="New (24h)" value={stats.users.new_last_24h} />
            </div>
          </div>
          <div>
            <h2 className="font-semibold mb-2">Content</h2>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
              <StatCard label="Courses" value={stats.content.courses} />
              <StatCard label="Lessons" value={stats.content.lessons} />
              <StatCard label="Quizzes" value={stats.content.quizzes} />
              <StatCard label="Certificates" value={stats.content.certificates} />
              <StatCard label="Notes" value={stats.content.notes} />
            </div>
          </div>
          <div>
            <h2 className="font-semibold mb-2">AI Usage</h2>
            <div className="grid grid-cols-2 gap-3">
              <StatCard label="Total chat messages" value={stats.ai_usage.total_chat_messages} />
              <StatCard label="Messages (24h)" value={stats.ai_usage.messages_last_24h} />
            </div>
          </div>
          <div>
            <h2 className="font-semibold mb-2">System</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              <StatCard label="Uploads storage" value={`${(stats.storage.uploads_bytes / 1024 / 1024).toFixed(1)} MB`} />
              <StatCard label="DB engine" value={stats.database.engine} />
              <StatCard
                label="DB health"
                value={stats.database.healthy ? `OK (${stats.database.latency_ms}ms)` : "Unhealthy"}
              />
            </div>
          </div>
        </div>
      )}

      {!loading && tab === "users" && (
        <div className="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left border-b border-slate-200 dark:border-slate-700 text-slate-500">
                <th className="p-3">Name</th>
                <th className="p-3">Email</th>
                <th className="p-3">Role</th>
                <th className="p-3">Status</th>
                <th className="p-3">Actions</th>
              </tr>
            </thead>
            <tbody>
              {users.map((u) => (
                <tr key={u.id} className="border-b border-slate-100 dark:border-slate-700/50">
                  <td className="p-3">{u.full_name}</td>
                  <td className="p-3">{u.email}</td>
                  <td className="p-3">
                    <select
                      value={u.role}
                      disabled={u.role === "super_admin" && !isSuperAdmin}
                      onChange={(e) => handleRoleChange(u.id, e.target.value)}
                      className="bg-transparent border border-slate-300 dark:border-slate-600 rounded-lg px-2 py-1"
                    >
                      {Object.keys(ROLE_LABELS)
                        .filter((r) => r !== "super_admin" || isSuperAdmin || u.role === "super_admin")
                        .map((r) => (
                          <option key={r} value={r}>{ROLE_LABELS[r]}</option>
                        ))}
                    </select>
                  </td>
                  <td className="p-3">
                    {u.is_deleted ? (
                      <span className="text-red-500">Deleted</span>
                    ) : u.is_active ? (
                      <span className="text-green-600">Active</span>
                    ) : (
                      <span className="text-slate-400">Disabled</span>
                    )}
                  </td>
                  <td className="p-3 space-x-2 whitespace-nowrap">
                    {!u.is_deleted && (
                      <>
                        <button onClick={() => handleToggleActive(u.id)} className="text-brand-600 hover:underline">
                          {u.is_active ? "Disable" : "Enable"}
                        </button>
                        {u.role !== "super_admin" && (
                          <button onClick={() => handleSoftDelete(u.id)} className="text-red-500 hover:underline">
                            Delete
                          </button>
                        )}
                      </>
                    )}
                    {u.is_deleted && (
                      <button onClick={() => handleRestore(u.id)} className="text-brand-600 hover:underline">
                        Restore
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {!loading && tab === "roles" && (
        <div className="space-y-4">
          {!isSuperAdmin && (
            <p className="text-sm text-slate-500">Only the Super Admin can edit permissions below (view only for you).</p>
          )}
          <div className="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left border-b border-slate-200 dark:border-slate-700 text-slate-500">
                  <th className="p-3">Permission</th>
                  {permCatalog.roles.map((r) => (
                    <th key={r} className="p-3">{ROLE_LABELS[r]}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {permCatalog.permissions.map((perm) => (
                  <tr key={perm} className="border-b border-slate-100 dark:border-slate-700/50">
                    <td className="p-3 font-mono text-xs">{perm}</td>
                    {permCatalog.roles.map((r) => {
                      const roleRow = roles.find((x) => x.role === r);
                      const allowed = roleRow?.permissions?.includes(perm);
                      return (
                        <td key={r} className="p-3">
                          <button
                            disabled={!isSuperAdmin}
                            onClick={() => handlePermToggle(r, perm, allowed)}
                            className={`h-5 w-5 rounded ${allowed ? "bg-brand-600" : "bg-slate-200 dark:bg-slate-600"} ${!isSuperAdmin ? "opacity-60" : ""}`}
                            aria-label={`${r} ${perm} ${allowed ? "allowed" : "denied"}`}
                          />
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {!loading && tab === "audit" && (
        <div className="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left border-b border-slate-200 dark:border-slate-700 text-slate-500">
                <th className="p-3">When</th>
                <th className="p-3">Actor</th>
                <th className="p-3">Action</th>
                <th className="p-3">Details</th>
              </tr>
            </thead>
            <tbody>
              {auditLogs.map((log) => (
                <tr key={log.id} className="border-b border-slate-100 dark:border-slate-700/50">
                  <td className="p-3 whitespace-nowrap">{new Date(log.created_at).toLocaleString()}</td>
                  <td className="p-3">{log.actor_name || "—"}</td>
                  <td className="p-3">{log.action}</td>
                  <td className="p-3 text-slate-500">{log.details || "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </Layout>
  );
}
