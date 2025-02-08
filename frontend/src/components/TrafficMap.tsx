import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Circle, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const TrafficMap: React.FC = () => {
  const [trafficData, setTrafficData] = useState<any[]>([]);
  const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    fetch(`${BACKEND_URL}/traffic`)
      .then((res) => res.json())
      .then((data) => setTrafficData(data))
      .catch((error) => console.error("Error al obtener tráfico:", error));
  }, []);

  return (
    <MapContainer center={[41.3851, 2.1734]} zoom={12} style={{ height: "500px", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {trafficData.map((point: any, index: number) => (
        <Circle
          key={index}
          center={[point.lat, point.lon]}
          radius={point.nivel * 100}
          pathOptions={{
            color: point.nivel > 7 ? "red" : point.nivel > 4 ? "orange" : "green",
          }}
        >
          <Popup>
            <b>{point.zona}</b> <br />
            Nivel de tráfico: {point.nivel}/10
          </Popup>
        </Circle>
      ))}
    </MapContainer>
  );
};

export default TrafficMap;