import {create} from 'zustand';

type ModelOutput = {
  Category: { [key: string]: number };
  SubMission: { [key: string]: number };
  Criticality: { [key: string]: number };
  Level: { [key: string]: number };
  Action: { [key: string]: number };
  Entity: { [key: string]: number };
  TaskObjective: { [key: string]: number };
  Constraints: { [key: string]: number };
  ObjectiveFunction: { [key: string]: number };
};

type Store = {
  l1Data: ModelOutput;
  l2Data: ModelOutput;
  setL1Data: (data: ModelOutput) => void;
  setL2Data: (data: ModelOutput) => void;
};

const useModelstore = create<Store>((set) => ({
  l1Data: {
    Category: {},
    SubMission: {},
    Criticality: {},
    Level: {},
    Action: {},
    Entity: {},
    TaskObjective: {},
    Constraints: {},
    ObjectiveFunction: {},
  },
  l2Data: {
    Category: {},
    SubMission: {},
    Criticality: {},
    Level: {},
    Action: {},
    Entity: {},
    TaskObjective: {},
    Constraints: {},
    ObjectiveFunction: {},
  },
  setL1Data: (data: ModelOutput) => set({ l1Data: data }),
  setL2Data: (data: ModelOutput) => set({ l2Data: data }),
}));
export default useModelstore;
