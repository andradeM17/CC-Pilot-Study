import numpy as np
import krippendorff
import numpy as np
import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa
from collections import Counter
from sklearn.metrics import cohen_kappa_score


files = ["Content", "Genre", "Topic", "Text Type"]

for x in range(len(files)):
    print(files[x])
    data = pd.read_csv(f"Pilot Study 2/IAA/GA/Files/{files[x]}.csv")
    data = data.values.tolist()  # Convert DataFrame to list of lists


    # Transpose: each row = annotator, each column = item
    transposed_data = list(map(list, zip(*data)))
    # Compute Krippendorff’s Alpha (nominal data)
    alpha = krippendorff.alpha(reliability_data=transposed_data, level_of_measurement='nominal')
    print("\tKrippendorff’s Alpha:", round(alpha, 4))


    # Separate the annotations from each annotator
    annotator1 = [row[0] for row in data]
    annotator2 = [row[1] for row in data]
    # Compute Cohen's Kappa
    kappa = cohen_kappa_score(annotator1, annotator2)
    print("\tCohen’s Kappa:", round(kappa, 4))


    # Step 1: Get all unique categories
    if x == 0:
        all_labels = [
            "Social media",
            "Website",
            "News",
            "Marketing",
            "Review",
            "Notice",
            "Legal",
            "Instructions",
            "Subtitles",
            "Literary",
            "Medical",
            "Didactic",
            "Historical",
            "Encyclopedia",
            "Other",
            "Blank"
        ]


    elif x == 1:
        all_labels = [
            "Search Results",
            "Forum",
            "Post",
            "Profile",
            "Feed",
            "Index",
            "Hard News",
            "Press Report",
            "Opinion Piece",
            "Interview",
            "Product Description",
            "Catalogue",
            "Media Review",
            "Product Review",
            "Service Review",
            "Experience Review",
            "Brochure",
            "Article",
            "Creative Nonfiction",
            "Guide",
            "How-to",
            "Recipe",
            "Online Help",
            "Search Query",
            "Homepage",
            "Boilerplate",
            "Fiction",
            "Blog",
            "Visual Entertainment",
            "Interview",
            "Audio Entertainment",
            "Talk",
            "Social Media",
            "Review Article",
            "Study Notes",
            "FAQ",
            "Exam",
            "Address",
            "Obituary",
            "Nonfiction",
            "Biography",
            "Object Biography",
            "Reference Material",
            "Feature Article",
            "Unclassified",
            "Legislation",
            "Report",
            "Newsletter",
            "Press release",
            "Blank"
        ]


    elif x == 2:
        all_labels = [
            "History",
            "Finance",
            "Politics",
            "Religion",
            "Personal Relationships",
            "Science",
            "Technology",
            "Culture & Entertainment",
            "Health",
            "Education",
            "Lifestyle & Recreation",
            "Nature & Environment",
            "Society & Demographics",
            "Legal",
            "Industry & Employment",
            "Blank"
        ]

    elif x == 3:
        all_labels = ["Descriptive", "Expository", "Narrative", "Persuasive / Argumentative", "Instructional", "Interrogative", "Blank"]

    elif x == 4:
        all_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    label_list = sorted(all_labels)  # consistent order
    # Step 2: Build item-category count matrix
    label_index = {label: idx for idx, label in enumerate(label_list)}
    # Initialize count matrix: rows = items, cols = categories
    counts = np.zeros((len(data), len(label_list)), dtype=int)
    for i, row in enumerate(data):
        counter = Counter(row)
        for label, count in counter.items():
            counts[i][label_index[label]] = count
    # Step 3: Compute Fleiss’ Kappa
    fleiss = fleiss_kappa(counts)
    print("\tFleiss’ Kappa:", round(fleiss, 4))


    print("\n\n")