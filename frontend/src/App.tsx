import { Navigate, Route, Routes } from "react-router-dom";

import { EstimatePage } from "./pages/estimate-page";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<EstimatePage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
