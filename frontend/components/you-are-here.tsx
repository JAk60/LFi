import { useEffect, useState } from "react";
import { middleOfUSA } from "../lib/constants";
import { Marker, useMap } from "@vis.gl/react-maplibre";
import { getLocation } from "../lib/api";

export default function YouAreHere() {
  const [markerLocation, setMarkerLocation] = useState(middleOfUSA);
  const { current: map } = useMap();

  useEffect(() => {
    if (!map) return;
    (async () => {
      const location = await getLocation();
      if (location !== middleOfUSA) {
        setMarkerLocation(location);
        map.flyTo({ center: location, zoom: 8 });
      }
    })();
  }, [map]);

  if (!map) return null;

  return (
    <Marker longitude={markerLocation[0]} latitude={markerLocation[1]}>
      <div
        style={{
          width: "24px",
          height: "24px",
          backgroundColor: "red",
          borderRadius: "50%",
          border: "2px solid white",
          boxShadow: "0 0 10px rgba(0, 0, 0, 0.5)",
        }}
      />
    </Marker>
  );
}
