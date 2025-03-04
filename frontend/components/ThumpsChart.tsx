import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  Cell,
} from "recharts";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";

// Function to get thumbs up count from local storage
const getThumbsUpCount = () => {
  const thumbsUpCount = localStorage.getItem("thumbsUpCount");
  return thumbsUpCount ? parseInt(thumbsUpCount, 10) : 0;
};
const getThumbsDownCount = () => {
  const thumbsDownCount = localStorage.getItem("thumbsDownCount");
  return thumbsDownCount ? parseInt(thumbsDownCount, 10) : 0;
};




const ThumbsChart = () => {
  const thumbsUpCount = getThumbsUpCount();
  const thumbsDownCount = getThumbsDownCount();
  const data = [
    { name: "Thumbs Up", count: thumbsUpCount, color: "green" },
    { name: "Thumbs Down", count: thumbsDownCount, color: "red" },
  ];
  return (
    <Card className="pb-[50px] mt-3 w-full h-[22rem] rounded-lg bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
      <CardHeader>
        <CardTitle className="text-white text-2xl">Thumbs Count</CardTitle>
      </CardHeader>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
        >
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" radius={[10, 10, 0, 0]}>
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.color} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
      {/* </CardContent> */}
    </Card>
  );
};

export default ThumbsChart;
