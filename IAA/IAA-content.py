import numpy as np
import krippendorff
import numpy as np
import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa
from collections import Counter
from sklearn.metrics import cohen_kappa_score


files = ["Content", "Genre", "Topic", "Text Type", "FTopic"]

for x in range(len(files)):
    print(files[x])
    data = pd.read_csv(f"IAA/Files/{files[x]}.csv")
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
            "Website",
            "Marketing",
            "Review",
            "Literary",
            "News",
            "Social media",
            "Encyclopedia",
            "Instructions",
            "Legal",
            "Encyclopaedia",
            "Subtitles",
            "Medical",
            "Historical",
            "Didactic",
            "Notice",
            "Reference material"
        ]

    elif x == 1:
        all_labels = [
            "Address",
            "Advertisement",
            "Audio entertainment",
            "Biography",
            "Blog",
            "Boiler plate text",
            "Book review",
            "Brochure",
            "Captions",
            "Catalogue",
            "Content Feed",
            "Creative non-fiction",
            "Dictionary entry",
            "Exam",
            "Feature article",
            "Fiction",
            "Forum",
            "Guide",
            "Hard news",
            "Homepage",
            "How-to",
            "Index",
            "Interview",
            "Listing",
            "Media review",
            "Non-fiction",
            "Obituary",
            "Object biography",
            "Object information",
            "Online help",
            "Opinion piece",
            "Post",
            "Press report",
            "Procedural information",
            "Product information",
            "Product review",
            "t (w/ or w/o Answer)",
            "Recipe",
            "Review article",
            "Search query",
            "Search results",
            "Service review",
            "Social media",
            "Study notes",
            "Talk",
            "User-generated content",
            "Visual entertainment",
            "Weather forecast"
        ]

    elif x == 2:
        all_labels = ["History", "Personal Relationships", "Technology and Digital Media", "Health and Medicine", "Politics and Governance", "Religion and Spirituality", "Entertainment and Media", "Education and Communication", "Lifestyle and Recreation", "Nature and Environment", "Society and Culture", "Philosophy and Abstract Concepts", "Specific Entities and References"]

    elif x == 3:
        all_labels = ["Descriptive", "Expository", "Narrative", "Persuasive / Argumentative", "Instructional", "Interrogative"]

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