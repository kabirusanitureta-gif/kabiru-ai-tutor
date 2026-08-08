import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout.jsx";
import { useAppSettings } from "../context/AppSettingsContext.jsx";
import { getCertificates, getCourses, certificateDownloadUrl } from "../api/endpoints.js";

export default function Certificates() {
  const { t } = useAppSettings();
  const [certificates, setCertificates] = useState([]);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;
    Promise.all([getCertificates(), getCourses()])
      .then(([certRes, coursesRes]) => {
        if (!isMounted) return;
        setCertificates(certRes.data);
        setCourses(coursesRes.data);
      })
      .catch(() => isMounted && setError("Could not load your certificates."))
      .finally(() => isMounted && setLoading(false));
    return () => {
      isMounted = false;
    };
  }, []);

  const courseTitleFor = (courseId) => {
    const course = courses.find((c) => c.id === courseId);
    return course ? course.title : "Course";
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold">{t("certificates")}</h1>
      <p className="text-slate-500 dark:text-slate-400 mt-1">
        Certificates are awarded automatically when you complete every lesson in a course.
      </p>

      {error && (
        <div className="mt-6 text-sm bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 px-4 py-3 rounded-xl">
          {error}
        </div>
      )}

      {loading ? (
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4 animate-pulse">
          {[1, 2].map((i) => (
            <div key={i} className="h-40 bg-slate-200 dark:bg-slate-800 rounded-2xl" />
          ))}
        </div>
      ) : certificates.length === 0 ? (
        <div className="card mt-6 text-center py-10">
          <div className="text-4xl mb-3">🎓</div>
          <p className="font-semibold">No certificates yet</p>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Complete every lesson in a course to earn your first certificate.
          </p>
          <Link to="/courses" className="btn-primary inline-block mt-4">
            {t("courses")}
          </Link>
        </div>
      ) : (
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
          {certificates.map((cert) => (
            <div key={cert.id} className="card">
              <div className="text-3xl">🏆</div>
              <h3 className="font-bold text-lg mt-2">{courseTitleFor(cert.course_id)}</h3>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                Certificate ID: {cert.certificate_code}
              </p>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                Issued: {new Date(cert.issued_at).toLocaleDateString()}
              </p>
              <a
                href={certificateDownloadUrl(cert.id)}
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary inline-block mt-4 text-sm"
              >
                {t("download")} PDF
              </a>
            </div>
          ))}
        </div>
      )}
    </Layout>
  );
}
