import json

# ---- Update file names here ----
file1 = "math_qwen.json"
file2 = "math_qwen_vllm_v3.json"
output_file = "math_qwen.json"
# --------------------------------

# Load the two JSON files
with open(file1, "r") as f:
    data1 = json.load(f)

with open(file2, "r") as f:
    data2 = json.load(f)

# Merge lists
combined = data1 + data2

# Remove entries with empty reasoning
combined = [item for item in combined if item.get("reasoning", "").strip() != ""]

# Remove duplicates (convert dicts to tuples so they are hashable)
unique = []
seen = set()

for item in combined:
    key = (
        item.get("question"),
        item.get("reasoning"),
        item.get("answer"),
    )
    if key not in seen:
        seen.add(key)
        unique.append(item)

# Save final result
with open(output_file, "w") as f:
    json.dump(unique, f, indent=2)

print(f"Done! Saved cleaned file to: {output_file}")
