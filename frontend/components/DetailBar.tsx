"use client"

import { Waves, Wind, Droplet } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

const seaState = {
  waveHeight: "2.5m",
  windSpeed: "15 Knots",
  humidity: "78%",
  condition: "Moderate Waves",
};

export function SeaStateWeather() {
  return (
    <Card className="h-full text-gray-200 flex flex-row items-center justify-between p-6 rounded-lg backdrop-blur-md bg-white/10 shadow-2xl border border-white/20 max-w-3xl">
      {/* Wave Height */}
      <div className="flex items-center gap-4">
        <Waves className="h-10 w-10 text-[#E8FF40]" />
        <div>
          <p className="text-xl font-bold text-white">{seaState.waveHeight}</p>
          <p className="text-gray-400 text-sm">Wave Height</p>
        </div>
      </div>
      
      {/* Wind Speed */}
      <div className="flex items-center gap-4">
        <Wind className="h-10 w-10 text-[#E8FF40]" />
        <div>
          <p className="text-xl font-bold text-white">{seaState.windSpeed}</p>
          <p className="text-gray-400 text-sm">Wind Speed</p>
        </div>
      </div>
      
      {/* Humidity */}
      <div className="flex items-center gap-4">
        <Droplet className="h-10 w-10 text-[#E8FF40]" />
        <div>
          <p className="text-xl font-bold text-white">{seaState.humidity}</p>
          <p className="text-gray-400 text-sm">Humidity</p>
        </div>
      </div>
      
      {/* Condition */}
      <div className="text-right">
        <p className="text-white text-2xl font-bold">{seaState.condition}</p>
        <p className="text-gray-400 text-sm">Current Condition</p>
      </div>
    </Card>
  );
}
