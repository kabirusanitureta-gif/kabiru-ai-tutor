import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";

// `roles`, if provided, restricts this route to users whose `role` is in
// the list (e.g. roles={["admin", "super_admin"]}). Omit it (the default
// for every existing route) to keep the old behavior: any authenticated
// user may access the route.
export default function ProtectedRoute({ children, roles }) {
  const { isAuthenticated, loading, user } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-white dark:bg-slate-900">
        <div className="animate-spin h-8 w-8 border-4 border-brand-500 border-t-transparent rounded-full" />
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  // Accounts created before email verification existed are backfilled to
  // is_verified=true, so this only ever applies to a brand new signup that
  // hasn't entered their PIN yet — every existing user's routes behave
  // exactly as before.
  if (user && user.is_verified === false) {
    return <Navigate to="/verify-email" replace />;
  }

  if (roles && roles.length > 0 && !roles.includes(user?.role)) {
    return <Navigate to="/dashboard" replace />;
  }

  return children;
}
