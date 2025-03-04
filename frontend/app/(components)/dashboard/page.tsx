"use client";

import { get_dependability } from "@/app/actions/dep";
import ThumbsChart from "@/components/ThumpsChart";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table";
import useModelstore from "@/store/ModelOutput";
import { Loader2, Send, ThumbsDown, ThumbsUp, X } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { startTransition, useActionState, useEffect, useState } from "react";

type DataProps = Record<string, number>;

type DashboardProps = {
  l1data: Record<string, DataProps>;
  l2data: Record<string, DataProps>;
};

const formatPercentage = (value: number): string =>
  `${(value * 100).toFixed(0)}%`;

type StateType = {
  systemDependability: number | null;
  equipmentDependability: number | null;
  loading: boolean;
  error: string | null;
};

export default function Dashboard() {
  const router = useRouter();
  const [userRole, setUserRole] = useState<string | null>(null);
  const l1data = useModelstore((state) => state.l1Data);
  const l2data = useModelstore((state) => state.l2Data);
  const [state, run, isPending] = useActionState(get_dependability, null);
  const [expandedItems, setExpandedItems] = useState<Record<string, boolean>>(
    {}
  );
  const [visibleRows, setVisibleRows] = useState<number>(8);
  const [showProceedButton, setShowProceedButton] = useState<boolean>(false);

  // Thumbs up and thumbs down counts
  const [thumbsUpCount, setThumbsUpCount] = useState<number>(0);
  const [thumbsDownCount, setThumbsDownCount] = useState<number>(0);

  // Load user role and thumbs counts from localStorage when component mounts
  useEffect(() => {
    const role = localStorage.getItem("user-role");
    setUserRole(role);

    const thumbsUp = localStorage.getItem("thumbsUpCount");
    const thumbsDown = localStorage.getItem("thumbsDownCount");

    setThumbsUpCount(thumbsUp ? parseInt(thumbsUp, 10) : 0);
    setThumbsDownCount(thumbsDown ? parseInt(thumbsDown, 10) : 0);
  }, []);

  // Improved ThumbsDown flow states
  const [showCategorySelectionDialog, setShowCategorySelectionDialog] =
    useState<boolean>(false);
  const [showSublabelDialog, setShowSublabelDialog] = useState<boolean>(false);
  const [selectedCategories, setSelectedCategories] = useState<
    Record<string, boolean>
  >({});
  const [currentCategoryIndex, setCurrentCategoryIndex] = useState<number>(0);
  const [selectedSublabels, setSelectedSublabels] = useState<
    Record<string, Record<string, boolean>>
  >({});
  const [modifiedL1Data, setModifiedL1Data] = useState<
    Record<string, DataProps>
  >({});

  const handleClick = (event: React.FormEvent) => {
    event.preventDefault();
    startTransition(() => {
      run();
      router.push("/result");
    });
  };

  function SubmitButton() {
    return (
      <Link href={"/result"}>
        <Button
          onClick={handleClick}
          type="submit"
          disabled={isPending}
          variant="outline"
          className="bg-[#FAE500] text-black p-6 text-lg border-gray-400 hover:bg-white"
        >
          {isPending ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Calculating...
            </>
          ) : (
            <>
              <Send className="mr-2 h-4 w-4" />
              Calculate Dependability
            </>
          )}
        </Button>
      </Link>
    );
  }

  if (!l1data || !l2data) {
    return (
      <div className="text-center text-lg font-semibold">No data available</div>
    );
  }

  const toggleExpandMasonry = (category: string, section: string) => {
    setExpandedItems((prev) => ({
      ...prev,
      [`${category}${section}`]: !prev[`${category}${section}`],
    }));
  };

  const totalL2Rows = Object.entries(l2data).reduce(
    (sum, values) => sum + Object.keys(values[1] || {}).length,
    0
  );
  const isTableExpanded = visibleRows >= totalL2Rows;

  const toggleExpandTable = () => {
    setVisibleRows(isTableExpanded ? 8 : totalL2Rows);
  };

  const handleThumbsUpClick = () => {
    const newCount = thumbsUpCount + 1;
    setThumbsUpCount(newCount);
    localStorage.setItem("thumbsUpCount", newCount.toString());
    setShowProceedButton(true);
  };

  const handleThumbsDownClick = () => {
    const newCount = thumbsDownCount + 1;
    setThumbsDownCount(newCount);
    localStorage.setItem("thumbsDownCount", newCount.toString());

    // Initialize selectedCategories with all categories set to false
    const initialCategorySelection = Object.keys(l1data).reduce(
      (acc, category) => {
        acc[category] = false;
        return acc;
      },
      {} as Record<string, boolean>
    );

    // Initialize selectedSublabels with all sublabels set to true (keep all by default)
    const initialSublabelSelection = Object.entries(l1data).reduce(
      (acc, [category, values]) => {
        acc[category] = Object.keys(values).reduce((subAcc, sublabel) => {
          subAcc[sublabel] = true;
          return subAcc;
        }, {} as Record<string, boolean>);
        return acc;
      },
      {} as Record<string, Record<string, boolean>>
    );

    setSelectedCategories(initialCategorySelection);
    setSelectedSublabels(initialSublabelSelection);
    setShowCategorySelectionDialog(true);
  };

  const handleCategoriesConfirm = () => {
    // Check if any categories were selected
    const hasSelectedCategories = Object.values(selectedCategories).some(
      (selected) => selected
    );

    if (!hasSelectedCategories) {
      // If no categories selected, show proceed button with original data
      setShowCategorySelectionDialog(false);
      setShowProceedButton(true);
      return;
    }

    // Get array of selected category names
    const categoriesToModify = Object.entries(selectedCategories)
      .filter(([_, selected]) => selected)
      .map(([category, _]) => category);

    // If categories are selected, proceed to sublabel selection
    setCurrentCategoryIndex(0);
    setShowCategorySelectionDialog(false);
    setShowSublabelDialog(true);
  };

  const handleCategoryToggle = (category: string) => {
    setSelectedCategories((prev) => ({
      ...prev,
      [category]: !prev[category],
    }));
  };

  const handleSublabelChange = (
    category: string,
    sublabel: string,
    checked: boolean
  ) => {
    setSelectedSublabels((prev) => ({
      ...prev,
      [category]: {
        ...prev[category],
        [sublabel]: checked,
      },
    }));
  };

  const handleSelectAllSublabels = (category: string, checked: boolean) => {
    setSelectedSublabels((prev) => ({
      ...prev,
      [category]: Object.keys(l1data[category]).reduce((acc, sublabel) => {
        acc[sublabel] = checked;
        return acc;
      }, {} as Record<string, boolean>),
    }));
  };

  const handleNextCategory = () => {
    const selectedCategoryNames = Object.entries(selectedCategories)
      .filter(([_, selected]) => selected)
      .map(([category, _]) => category);

    if (currentCategoryIndex < selectedCategoryNames.length - 1) {
      setCurrentCategoryIndex(currentCategoryIndex + 1);
    } else {
      // Apply changes and finish
      applyChangesToL1Data();
      setShowSublabelDialog(false);
      setShowProceedButton(true);
    }
  };

  const handlePreviousCategory = () => {
    if (currentCategoryIndex > 0) {
      setCurrentCategoryIndex(currentCategoryIndex - 1);
    }
  };

  const handleCancel = () => {
    // Reset all states and close dialogs
    setShowCategorySelectionDialog(false);
    setShowSublabelDialog(false);
    setSelectedCategories({});
    setSelectedSublabels({});
  };

  const applyChangesToL1Data = () => {
    // Create a copy of the original l1data
    const updatedL1Data = { ...l1data };

    // Only modify the selected categories
    Object.entries(selectedCategories).forEach(([category, isSelected]) => {
      if (isSelected) {
        // For selected categories, filter sublabels based on user selection
        updatedL1Data[category] = Object.keys(selectedSublabels[category])
          .filter((sublabel) => selectedSublabels[category][sublabel])
          .reduce((obj, sublabel) => {
            obj[sublabel] = l1data[category][sublabel];
            return obj;
          }, {} as DataProps);
      }
    });

    setModifiedL1Data(updatedL1Data);
  };

  const getFilteredL1Data = () => {
    return Object.keys(modifiedL1Data).length > 0 ? modifiedL1Data : l1data;
  };

  // Get the current category name based on selection and index
  const getCurrentCategoryName = () => {
    return Object.entries(selectedCategories)
      .filter(([_, selected]) => selected)
      .map(([category, _]) => category)[currentCategoryIndex];
  };

  // Calculate progress for the progress bar
  const calculateProgress = () => {
    const selectedCategoryCount =
      Object.values(selectedCategories).filter(Boolean).length;
    if (selectedCategoryCount === 0) return 0;
    return Math.round(
      ((currentCategoryIndex + 1) / selectedCategoryCount) * 100
    );
  };
  // Function to get category-grouped data for the table
  const getGroupedTableData = () => {
    const data = showProceedButton ? getFilteredL1Data() : l1data;

    return Object.entries(data)
      .flatMap(([category, values]) =>
        Object.entries(values).map(([subCategory, value]) => [
          category,
          subCategory,
          value,
        ])
      )
      .slice(0, visibleRows);
  };
  if (userRole === "trainer") {
    console.log("statestatestatestatestatestate", state);
    return (
      <div className="p-6 w-full flex gap-4 justify-center items-center min-h-screen bg-neutral-900">
        <div className="w-2/3 max-w-xl">
          <Card className="rounded-lg bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
            <CardHeader>
              <CardTitle className="text-3xl font-semibold text-gray-100">
                Extracted Context
              </CardTitle>
              <CardDescription className="text-gray-400">
                Detailed breakdown of all Extracted Context headers
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableBody>
                    {(() => {
                      const tableData = getGroupedTableData();
                      let previousCategory = "";
                      let categoryRowCount = 0;

                      return tableData.map((row, index) => {
                        const [category, subCategory, value] = row;
                        const isNewCategory = category !== previousCategory;
                        const isLastInCategory =
                          index === tableData.length - 1 ||
                          tableData[index + 1][0] !== category; // Check if next row has a different category

                        // Update tracking variables
                        if (isNewCategory) {
                          previousCategory = category;
                          categoryRowCount = 1;
                        } else {
                          categoryRowCount++;
                        }

                        return (
                          <TableRow
                            key={`${category}-${subCategory}-${index}`}
                            className={`text-gray-200 text-sm border-l-4 border-r-4 border-gray-600 ${
                              isNewCategory ? "border-t-4 border-gray-500" : ""
                            } ${
                              isLastInCategory
                                ? "border-b-4 border-gray-500"
                                : ""
                            }`}
                          >
                            <TableCell
                              className={`${
                                isNewCategory
                                  ? "font-bold text-gray-100 bg-gray-700 border-l-4 border-[#FAE500]"
                                  : "border-l-2 border-gray-600"
                              }`}
                            >
                              {category}
                            </TableCell>
                            <TableCell>{subCategory}</TableCell>
                            <TableCell className="text-right font-semibold">
                              {formatPercentage(value)}
                            </TableCell>
                          </TableRow>
                        );
                      });
                    })()}
                  </TableBody>
                </Table>
              </div>
              <div className="flex justify-center mt-4">
                <Button onClick={toggleExpandTable} variant="outline">
                  {isTableExpanded ? "Show Less" : "Show More"}
                </Button>
              </div>
              <div className="mt-9 flex gap-3 justify-center mb-4">
                <Button
                  onClick={handleThumbsUpClick}
                  variant="outline"
                  className="bg-green-400"
                >
                  <ThumbsUp />
                </Button>
                <Button
                  onClick={handleThumbsDownClick}
                  variant="outline"
                  className="bg-red-400"
                >
                  <ThumbsDown />
                </Button>
              </div>

              {showProceedButton && (
                <div className="flex justify-center mt-4">
                  <SubmitButton />
                </div>
              )}
            </CardContent>
          </Card>
        </div>
        {/* Added ThumbsChart for trainer role */}
        <div className="mt-6 w-1/3">
          <ThumbsChart />
        </div>

        {/* Add the dialogs here for the trainer role as well */}
        {/* Category Selection Dialog */}
        {showCategorySelectionDialog && (
          <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <Card className="w-full max-w-md p-6 bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
              <CardHeader className="flex flex-row items-center justify-between">
                <CardTitle className="text-xl font-bold text-gray-100">
                  Which categories would you like to modify?
                </CardTitle>
                <Button
                  variant="ghost"
                  onClick={handleCancel}
                  className="h-8 w-8 p-0 rounded-full"
                >
                  <X className="h-4 w-4 text-gray-200" />
                </Button>
              </CardHeader>
              <CardContent>
                <div className="space-y-3 mb-6">
                  {Object.keys(l1data).map((category) => (
                    <div
                      key={category}
                      className="flex items-center text-gray-200 text-lg"
                    >
                      <input
                        type="checkbox"
                        id={`category-${category}`}
                        checked={selectedCategories[category] || false}
                        onChange={() => handleCategoryToggle(category)}
                        className="mr-3 h-5 w-5"
                      />
                      <label htmlFor={`category-${category}`}>{category}</label>
                    </div>
                  ))}
                </div>
                <div className="flex justify-between mt-6">
                  <Button
                    onClick={handleCancel}
                    variant="outline"
                    className="border-gray-400 text-gray-200 hover:bg-gray-700"
                  >
                    Cancel
                  </Button>
                  <Button
                    onClick={handleCategoriesConfirm}
                    variant="outline"
                    className="bg-[#FAE500] text-black border-gray-400 hover:bg-white"
                  >
                    Continue
                  </Button>
                </div>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Sublabel Selection Dialog */}
        {showSublabelDialog && (
          <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <Card className="w-full max-w-md p-6 bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
              <CardHeader>
                <div className="flex justify-between items-center">
                  <CardTitle className="text-xl font-bold text-[#FAE500]">
                    {getCurrentCategoryName()}
                  </CardTitle>
                  <Button
                    variant="ghost"
                    onClick={handleCancel}
                    className="h-8 w-8 p-0 rounded-full"
                  >
                    <X className="h-4 w-4 text-gray-200" />
                  </Button>
                </div>
                {/* Progress bar */}
                <div className="w-full bg-gray-700 h-2 rounded-full mt-4">
                  <div
                    className="bg-[#FAE500] h-2 rounded-full"
                    style={{ width: `${calculateProgress()}%` }}
                  ></div>
                </div>
                <div className="text-gray-400 text-sm mt-1">
                  Category {currentCategoryIndex + 1} of{" "}
                  {Object.values(selectedCategories).filter(Boolean).length}
                </div>
              </CardHeader>
              <CardContent>
                <div className="mb-3 flex items-center">
                  <Button
                    variant="outline"
                    size="sm"
                    className="mr-2 text-xs"
                    onClick={() =>
                      handleSelectAllSublabels(getCurrentCategoryName(), true)
                    }
                  >
                    Select All
                  </Button>
                  <Button
                    variant="outline"
                    size="sm"
                    className="text-xs"
                    onClick={() =>
                      handleSelectAllSublabels(getCurrentCategoryName(), false)
                    }
                  >
                    Deselect All
                  </Button>
                </div>
                <div className="space-y-2 max-h-60 overflow-y-auto mt-2">
                  {Object.entries(l1data[getCurrentCategoryName()]).map(
                    ([key, value]) => (
                      <div
                        key={key}
                        className="flex items-center text-gray-200 text-lg"
                      >
                        <input
                          type="checkbox"
                          id={`sublabel-${key}`}
                          checked={
                            selectedSublabels[getCurrentCategoryName()]?.[
                              key
                            ] || false
                          }
                          onChange={(e) =>
                            handleSublabelChange(
                              getCurrentCategoryName(),
                              key,
                              e.target.checked
                            )
                          }
                          className="mr-2"
                        />
                        <label htmlFor={`sublabel-${key}`} className="flex-1">
                          {key}: {formatPercentage(value)}
                        </label>
                      </div>
                    )
                  )}
                </div>
                <div className="flex justify-between mt-6">
                  <Button
                    onClick={handlePreviousCategory}
                    variant="outline"
                    className="border-gray-400 text-gray-200 hover:bg-gray-700"
                    disabled={currentCategoryIndex === 0}
                  >
                    Previous
                  </Button>
                  <Button
                    onClick={handleNextCategory}
                    variant="outline"
                    className="bg-[#FAE500] text-black border-gray-400 hover:bg-white"
                  >
                    {currentCategoryIndex ===
                    Object.values(selectedCategories).filter(Boolean).length - 1
                      ? "Finish"
                      : "Next"}
                  </Button>
                </div>
              </CardContent>
            </Card>
          </div>
        )}
      </div>
    );
  }

  // Standard view for non-trainer roles - display the original UI
  return (
    <div className="p-6 w-full space-y-6 bg-neutral-900">
      <div className="grid grid-cols-1 md:grid-cols-6 gap-6">
        <div className="md:col-span-4">
          <div className="columns-2 gap-6 space-y-6 [&>*:not(:first-child)]:mt-6">
            {Object.entries(l1data).map(([category, values]) => {
              const l1Items = Object.entries(values);
              const l1ItemsToShow = expandedItems[`${category}l1`]
                ? l1Items
                : l1Items.slice(0, 3);
              const showL1MoreButton = l1Items.length > 3;

              const l2Items = Object.entries(l2data[category] || {});
              const l2ItemsToShow = expandedItems[`${category}l2`]
                ? l2Items
                : l2Items.slice(0, 3);
              const showL2MoreButton = l2Items.length > 3;

              return (
                <div key={category} className="break-inside-avoid">
                  <Card className="rounded-lg bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
                    <CardHeader>
                      <CardTitle className="text-lg font-bold tracking-wide uppercase text-gray-200">
                        {category}
                      </CardTitle>
                    </CardHeader>
                    <CardContent className="flex flex-col">
                      <div className="grid grid-cols-2 gap-4">
                        <div>
                          <div className="text-xl font-semibold text-[#FAE500]">
                            NN
                          </div>
                          <div className="space-y-2">
                            {l1ItemsToShow.map(([key, value]) => (
                              <div key={key} className="text-gray-200 text-lg">
                                {key}: {formatPercentage(value)}
                              </div>
                            ))}
                          </div>
                          {showL1MoreButton && (
                            <button
                              onClick={() =>
                                toggleExpandMasonry(category, "l1")
                              }
                              className="text-blue-500 hover:underline mt-2"
                            >
                              {expandedItems[`${category}l1`]
                                ? "Show Less"
                                : "Show More"}
                            </button>
                          )}
                        </div>
                        <div>
                          {l2Items.length > 0 && (
                            <div>
                              <div className="text-xl font-semibold text-[#FAE500]">
                                LF
                              </div>
                              <div className="space-y-2">
                                {l2ItemsToShow.map(([key, value]) => (
                                  <div
                                    key={key}
                                    className="text-gray-200 text-lg"
                                  >
                                    {key}: {formatPercentage(value)}
                                  </div>
                                ))}
                              </div>
                              {showL2MoreButton && (
                                <button
                                  onClick={() =>
                                    toggleExpandMasonry(category, "l2")
                                  }
                                  className="text-blue-500 hover:underline mt-2"
                                >
                                  {expandedItems[`${category}l2`]
                                    ? "Show Less"
                                    : "Show More"}
                                </button>
                              )}
                            </div>
                          )}
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              );
            })}
          </div>
        </div>
        <div className="md:col-span-2">
          <Card className="rounded-lg bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
            <CardHeader>
              <CardTitle className="text-3xl font-semibold text-gray-100">
                Extracted Context
              </CardTitle>
              <CardDescription className="text-gray-400">
                Detailed breakdown of all Extracted Context headers
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableBody>
                    {(() => {
                      const tableData = getGroupedTableData();
                      let previousCategory = "";
                      let categoryRowCount = 0;

                      return tableData.map((row, index) => {
                        const [category, subCategory, value] = row;
                        const isNewCategory = category !== previousCategory;
                        const isLastInCategory =
                          index === tableData.length - 1 ||
                          tableData[index + 1][0] !== category; // Check if next row has a different category

                        // Update tracking variables
                        if (isNewCategory) {
                          previousCategory = category;
                          categoryRowCount = 1;
                        } else {
                          categoryRowCount++;
                        }

                        return (
                          <TableRow
                            key={`${category}-${subCategory}-${index}`}
                            className={`text-gray-200 text-sm border-l-4 border-r-4 border-gray-600 ${
                              isNewCategory ? "border-t-4 border-gray-500" : ""
                            } ${
                              isLastInCategory
                                ? "border-b-4 border-gray-500"
                                : ""
                            }`}
                          >
                            <TableCell
                              className={`${
                                isNewCategory
                                  ? "font-bold text-gray-100 bg-gray-700 border-l-4 border-[#FAE500]"
                                  : "border-l-2 border-gray-600"
                              }`}
                            >
                              {category}
                            </TableCell>
                            <TableCell>{subCategory}</TableCell>
                            <TableCell className="text-right font-semibold">
                              {formatPercentage(value)}
                            </TableCell>
                          </TableRow>
                        );
                      });
                    })()}
                  </TableBody>
                </Table>
              </div>
              <div className="flex justify-center mt-4">
                <Button onClick={toggleExpandTable} variant="outline">
                  {isTableExpanded ? "Show Less" : "Show More"}
                </Button>
              </div>
              <div className="mt-9 flex gap-3 justify-center mb-4">
                <Button
                  onClick={handleThumbsUpClick}
                  variant="outline"
                  className="bg-green-400"
                >
                  <ThumbsUp />
                </Button>
                <Button
                  onClick={handleThumbsDownClick}
                  variant="outline"
                  className="bg-red-400"
                >
                  <ThumbsDown />
                </Button>
              </div>
            </CardContent>
          </Card>
          {showProceedButton ? (
            <div className="z-11 relative flex justify-center mt-4">
              <SubmitButton />
            </div>
          ) : (
            ""
          )}
          <ThumbsChart />
        </div>
      </div>

      {/* Category Selection Dialog */}
      {showCategorySelectionDialog && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <Card className="w-full max-w-md p-6 bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
            <CardHeader className="flex flex-row items-center justify-between">
              <CardTitle className="text-xl font-bold text-gray-100">
                Which categories would you like to modify?
              </CardTitle>
              <Button
                variant="ghost"
                onClick={handleCancel}
                className="h-8 w-8 p-0 rounded-full"
              >
                <X className="h-4 w-4 text-gray-200" />
              </Button>
            </CardHeader>
            <CardContent>
              <div className="space-y-3 mb-6">
                {Object.keys(l1data).map((category) => (
                  <div
                    key={category}
                    className="flex items-center text-gray-200 text-lg"
                  >
                    <input
                      type="checkbox"
                      id={`category-${category}`}
                      checked={selectedCategories[category] || false}
                      onChange={() => handleCategoryToggle(category)}
                      className="mr-3 h-5 w-5"
                    />
                    <label htmlFor={`category-${category}`}>{category}</label>
                  </div>
                ))}
              </div>
              <div className="flex justify-between mt-6">
                <Button
                  onClick={handleCancel}
                  variant="outline"
                  className="border-gray-400 text-gray-200 hover:bg-gray-700"
                >
                  Cancel
                </Button>
                <Button
                  onClick={handleCategoriesConfirm}
                  variant="outline"
                  className="bg-[#FAE500] text-black border-gray-400 hover:bg-white"
                >
                  Continue
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
      {/* Sublabel Selection Dialog */}
      {showSublabelDialog && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <Card className="w-full max-w-md p-6 bg-gray-400 bg-clip-padding backdrop-filter backdrop-blur-sm bg-opacity-10 border border-gray-100">
            <CardHeader>
              <div className="flex justify-between items-center">
                <CardTitle className="text-xl font-bold text-[#FAE500]">
                  {getCurrentCategoryName()}
                </CardTitle>
                <Button
                  variant="ghost"
                  onClick={handleCancel}
                  className="h-8 w-8 p-0 rounded-full"
                >
                  <X className="h-4 w-4 text-gray-200" />
                </Button>
              </div>
              {/* Progress bar */}
              <div className="w-full bg-gray-700 h-2 rounded-full mt-4">
                <div
                  className="bg-[#FAE500] h-2 rounded-full"
                  style={{ width: `${calculateProgress()}%` }}
                ></div>
              </div>
              <div className="text-gray-400 text-sm mt-1">
                Category {currentCategoryIndex + 1} of{" "}
                {Object.values(selectedCategories).filter(Boolean).length}
              </div>
            </CardHeader>
            <CardContent>
              <div className="mb-3 flex items-center">
                <Button
                  variant="outline"
                  size="sm"
                  className="mr-2 text-xs"
                  onClick={() =>
                    handleSelectAllSublabels(getCurrentCategoryName(), true)
                  }
                >
                  Select All
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  className="text-xs"
                  onClick={() =>
                    handleSelectAllSublabels(getCurrentCategoryName(), false)
                  }
                >
                  Deselect All
                </Button>
              </div>
              <div className="space-y-2 max-h-60 overflow-y-auto mt-2">
                {Object.entries(l1data[getCurrentCategoryName()]).map(
                  ([key, value]) => (
                    <div
                      key={key}
                      className="flex items-center text-gray-200 text-lg"
                    >
                      <input
                        type="checkbox"
                        id={`sublabel-${key}`}
                        checked={
                          selectedSublabels[getCurrentCategoryName()]?.[key] ||
                          false
                        }
                        onChange={(e) =>
                          handleSublabelChange(
                            getCurrentCategoryName(),
                            key,
                            e.target.checked
                          )
                        }
                        className="mr-2"
                      />
                      <label htmlFor={`sublabel-${key}`} className="flex-1">
                        {key}: {formatPercentage(value)}
                      </label>
                    </div>
                  )
                )}
              </div>
              <div className="flex justify-between mt-6">
                <Button
                  onClick={handlePreviousCategory}
                  variant="outline"
                  className="border-gray-400 text-gray-200 hover:bg-gray-700"
                  disabled={currentCategoryIndex === 0}
                >
                  Previous
                </Button>
                <Button
                  onClick={handleNextCategory}
                  variant="outline"
                  className="bg-[#FAE500] text-black border-gray-400 hover:bg-white"
                >
                  {currentCategoryIndex ===
                  Object.values(selectedCategories).filter(Boolean).length - 1
                    ? "Finish"
                    : "Next"}
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
}
