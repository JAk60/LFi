"use client";
import { Html, OrbitControls, useProgress } from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";
import { Suspense, useEffect, useRef, useState } from "react";
import { Vector3 } from "three";
import Model from "./Model";

import YouAreHere from "@/components/you-are-here";
import { Map } from "@vis.gl/react-maplibre";
import { ScoreChart } from "./depoutput";
import { SeaStateWeather } from "./DetailBar";
import SentenceDisplay from "./ScenarioText";

function Loader() {
  const { progress } = useProgress();
  return <Html center>{progress.toFixed(1)} % loaded</Html>;
}

// Animated wrapper for the model
function AnimatedModel() {
  const modelRef = useRef();
  const [isExpanded, setIsExpanded] = useState(false);
  const initialScale = new Vector3(0.8, 0.8, 0.8);
  const expandedScale = new Vector3(1, 1, 1);
  
  // Handle initial expansion animation
  useEffect(() => {
    const timer = setTimeout(() => setIsExpanded(true), 500);
    return () => clearTimeout(timer);
  }, []);

  useFrame((state, delta) => {
    if (!modelRef.current) return;

    // Smooth scale animation
    const targetScale = isExpanded ? expandedScale : initialScale;
    modelRef.current.scale.lerp(targetScale, 0.05);

    // Gentle continuous rotation
    modelRef.current.rotation.y += delta * 0.2; // Adjust speed by changing this value
  });

  return (
    <group ref={modelRef} scale={initialScale}>
      <Model />
    </group>
  );
}
type SceneProps = {
  systemDependability: number;
  equipmentDependability: number[];
};


export default function Scene() {
  // const { setDependabilityData } = useDependabilityStore();
  // setDependabilityData(depvalue);
  return (
    <div className="ml-8 h-screen w-[100%] p-4">
      <div className="flex gap-4 h-full">
        {/* Left Column */}
        <div className="w-1/2 flex flex-col gap-4">
          {/* Details Card */}
          <div className="h-1/3 rounded-lg backdrop-blur-md bg-white/10 p-4 shadow-xl border border-white/20">
            <SentenceDisplay />
          </div>
          {/* Canvas Card */}
          <div className="h-2/3 rounded-lg ">
          <Canvas
            style={{
              height: "100%",
              background: "rgba(255, 255, 255, 0.1)", // Light transparent background
              borderRadius: "0.75rem",
              backdropFilter: "blur(4px)", // Blur effect
              // WebkitBackdropFilter: "blur(10px)", // For Safari support
              border: "1px solid rgba(255, 255, 255, 0.2)", // Subtle border for glass effect
            }}
          >
            <ambientLight intensity={10} />
            <directionalLight position={[5, 5, 5]} intensity={5} />
            <pointLight position={[-5, -5, -5]} intensity={5} />
            <spotLight
              position={[5, 5, 5]}
              angle={0.3}
              penumbra={1}
              intensity={5}
              castShadow
            />
            <Suspense fallback={<Loader />}>
              <AnimatedModel />
              <OrbitControls
                dampingFactor={0.05}
                enableZoom={true}
                enablePan={true}
                enableRotate={true}
                autoRotate={false}
              />
            </Suspense>
          </Canvas>
          </div>
          {/* Details Card */}
          <div className="h-1/3 rounded-lg backdrop-blur-md bg-white/10 p-4 shadow-xl border border-white/20">
            <SeaStateWeather />
          </div>
        </div>

        {/* Right Column */}
        <div className="w-[48%] h-full flex flex-col gap-4">
          {/* Map Card */}
          <div className="h-1.5/3 rounded-lg overflow-hidden backdrop-blur-md bg-white/10 shadow-xl border border-white/20">
            <Map
              initialViewState={{
                longitude: 72.993477,
                latitude: 19.157934,
                zoom: 8,
                pitch: 0,
                bearing: 0,
              }}
              mapStyle="/styles/dark.json"
              style={{ width: "100%", height: "100%" }}
              interactive={true}
              dragRotate={false}
              touchZoomRotate={false}
              maxZoom={10}
              minZoom={6}
            >
              <YouAreHere />
            </Map>
          </div>
          {/* Bottom Details Card */}
          <ScoreChart />
        </div>
      </div>
    </div>
  );
}