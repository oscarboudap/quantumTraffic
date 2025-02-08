import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const Dashboard: React.FC = () => {
  const [trafficData, setTrafficData] = useState<any[]>([]);
  const [alerts, setAlerts] = useState<string | null>(null);
  const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    fetch(`${BACKEND_URL}/traffic`)
      .then((res) => res.json())
      .then((data) => setTrafficData(data))
      .catch((error) => console.error("Error al obtener tráfico:", error));
  }, []);

  return (
    <div>
      <h2>📊 Tráfico en Tiempo Real</h2>
      <LineChart width={500} height={300} data={trafficData}>
        <XAxis dataKey="zona" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Line type="monotone" dataKey="nivel" stroke="#ff0000" />
      </LineChart>
      {alerts && <h2 style={{ color: "red" }}>🚨 {alerts}</h2>}
    </div>
  );
};

export default Dashboard;