// types/data.ts
export interface ModelData {
    category?: Record<string, number>;
    'sub category'?: Record<string, number>;
    criticality?: Record<string, number>;
    Level?: Record<string, number>;
    Action?: Record<string, number>;
    Entity?: Record<string, number>;
    From?: Record<string, number>;
    'Task Objective'?: Record<string, number>;
    Constraints?: Record<string, number>;
    'Objective function'?: Record<string, number>;
  }
  
  export interface ChartDataPoint {
    name: string;
    value: number;
  }
  
  // data.ts
  export const l1Data: ModelData = {
    category: {
      'Maintenance': 0.21521792940360723,
      'Mission': 0.7847820705963928
    },
    'sub category': {
      'Combat': 0.30591673665833197,
      'Exercise': 0.4071113560616829,
      'Fleet Support': 0.06905356986846138,
      'Humanitarian': 0.07520728297857408,
      'Miscellaneous': 0.09108950394584861,
      'Sortie': 0.05162155048710088
    },
    criticality: { 
      "High": 0.7702515640373945, 
      "Low": 0.22974843596260563 
    },
    Level: {
      "Equipment": 0.1556215306253924,
      "Fleet": 0.36884622577328074,
      "Ship": 0.47553224360132695
    },
    Action: {
      "Evaluate": 0.735941575160418,
      "Identify": 0.22774022609256628,
      "Select K out of N": 0.03631819874701576
    },
    Entity: {
      "Equipment": 0.11150942893103581,
      "Ship": 0.8720510736425374,
      "Workshop": 0.016439497426426686
    },
    From: {
      "Equipment": 0.08624834905026696,
      "Fleet": 0.49924794123632366,
      "Ships": 0.38026011318053504,
      "Workshops": 0.03424359653287435
    },
    'Task Objective': {
      "Gun firing": 0.16470268795959278,
      "Interrogation and interception": 0.5032645550989358,
      "Maintenance scheduling": 0.14228827897676963,
      "Miscellaneous": 0.03647252200949749,
      "Missile firing": 0.03982868568065387,
      "Search and rescue": 0.11344327027455045
    },
    Constraints: {
      "Activity sequences": 0.12608804829775797,
      "Balancing loads": 0.28981810337634817,
      "Capability": 0.021296575206008618,
      "Conformance": 0.0474731903550879,
      "Endurance": 0.043613237759537925,
      "Fleet availability": 0.022900508949690895,
      "Fuel": 0.06570551561304591,
      "Logistic time": 0.053470522941375484
    },
    'Objective function': {
      "Maximum availability": 0.1541919462134113,
      "Maximum conformance": 0.39730072525686405,
      "Maximum reliability": 0.030626259062906353,
      "Minimum cost": 0.20609613163467694,
      "Minimum downtime": 0.05998688216793612,
      "Minimum risk": 0.08829403182944907,
      "Minimum time": 0.06350402383475622
    }
  };
  
  export const l2Data: ModelData = {
    // Copy l1Data structure and replace with L2 values
    ...l1Data  // Replace with actual L2 data
  };
  