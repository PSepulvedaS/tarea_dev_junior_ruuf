from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    best_quantity = 0
    roof_area = roof_width * roof_height
    panel_area = panel_width * panel_height
    orientations = [(panel_width, panel_height), (panel_height, panel_width)]

    for orientation in orientations:
        panels_per_row = roof_width // orientation[0]
        panels_per_column = roof_height // orientation[1]
        total_panels = panels_per_row * panels_per_column

        roof_area_used = total_panels * panel_area

        if roof_area_used < roof_area:
            new_roof_height = roof_height - (panels_per_column * orientation[1])

            if roof_width >= orientation[1] and new_roof_height >= orientation[0]:
                reoriented_panels_per_row = roof_width // orientation[1]
                reoriented_panels_per_column = new_roof_height // orientation[0]
                additional_panels = reoriented_panels_per_row * reoriented_panels_per_column
                total_panels += additional_panels

        if total_panels > best_quantity:
            best_quantity = total_panels
    
    return best_quantity


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
