---
layout: single
title:  "log on tricks"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
categories: 
  - Jekyll
tags:
  - python
---

Python misc commands
---
1. View attributes and values for object 

```python
  from pprint import pprint
  pprint(vars(PythonObject))
```

2. Query pathes recursively from a given folder

```python
  import glob
  allpathes_infolder = [filename for filename in glob.iglob(foldername + '/**/**', recursive = True)]
```

3. save csv file line by line in loop

package requirement csv

```python
  import csv
  cols_headernames = [str] # list of strings
  savefilename = str

  # step 1: write the header to csv
  with open(savefilename , "w") as file:
    writer = csv.DictWriter(file, fieldnames = cols_headernames)
    writer.writeheader()

  # step 2: write csv row by row
  # generic for-loop that generates row (or rows) 
  for iter in range(n):
    rows_returns_from_each_iter = somefunc(iter)

    with open(savefilename, "a+", newline='') as file:
      writer=csv.writer(file)
      # if it is a single row []
      if len(rows_returns_from_each_iter) == 1:
        writer.writerrows([rows_returns_from_each_iter])
      # if it is multiple rows: lists of list [[]]
      elif len(rows_returns_from_each_iter) > 1:
        writer.writerrows(rows_returns_from_each_iter)
```