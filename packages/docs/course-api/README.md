---
sidebar: auto
---

# Unified Backend

## Overview

![Backend Architecture](./backend-architecture.png)

The Unified Backend provides unified access to UofT course data scattered across UofT's web services. The API relies on three main sources [UofT Course Finder](#_1-uoft-course-finder), [UTM Academic Calendar](#_2-utm-academic-calendar), [UTM Program Selection Guide](#_3-utm-program-selection-guide) , and [UTM Course Evaluations](#_4-utm-course-evaluations). 

## Data Sources

### 1. [UofT Course Finder:](http://coursefinder.utoronto.ca/course-search/search/courseSearch?viewId=CourseSearch-FormView&methodToCall=start)

__Data Provided:__ Information regarding every course in all 3 UofT campuses. Information such as lecture time, professors, pre-requisite etc are provided (refer to [**Data Structures 1-3**](#_1-course) for details). 

### 2. [UTM Academic Calendar:](https://student.utm.utoronto.ca/calendar/program_list.pl)

__Data Provided:__ Information regarding every program in UTM. Information such as post requirement, required courses, program level (minor, major, specialist) etc are provided (refer to [**Data Structures 4-5**](#_4-subject) for details). 

### 3. [UTM Program Selection Guide:](https://www.utm.utoronto.ca/registrar/office-registrar-publications/program-selection-guide)

__Data Provided:__ Program type (1, 2, 3) for every UTM program. This information is stored as a attribute in [**Data Structures 5, Program**](#_5-program).

### 4. [UTM Course Evaluations:](https://course-evals.utoronto.ca/BPI/fbview.aspx?blockid=hjeZ7JJWJupVgjPoyu&userid=tO4GQugFiFULB0AXgInh7idHCU-AnN3pNhvC&lng=en)

__Data Provided:__ Course evaluation results for UTM Mississauga Undergraduate Programs (refer to [**Data Structure 6**](#_6-course-evaluation)).

## Scraper Breakdown

### 1. UTM Course Scraper:
The scraper takes data from [**Data Source, UofT Course Finder**](#_1-uoft-course-finder) then every single course with the code *H5* is placed into a queue. Each of the threads extract a course and scrape the relevant data (refer to [**Data Structures 1-3**](#_1-course) for details). 

### 2. UTM Program Scraper:
The scraper takes data from [**Data Source, UTM Academic Calendar**](#_2-utm-academic-calendar) then the data are placed into 2 objects (refer to [**Data Structures 4-5**](#_4-subject) for details). The data is used for the course guide API to provide recommended courses.

### 3. Course Evaluation Scraper
The scraper takes data from [**Data Source, UTM Course Evaluations**](#_4-utm-course-evaluations).

Items 1-9 are criteria with responses that range from 1 to 5, with 1 as the lowest rating and 5 as the highest rating.
* **item 1:** I found the course intellectually stimulating.
* **item 2:** The course provided me with a deeper understanding of the subject matter.
* **item 3:** The instructor created a course atmosphere that was conducive to my learning.
* **item 4:** Course projects, assignments, tests and/or exams improved my understanding of the course material.
* **item 5:** Course projects, assignments, tests and/or exams provided opportunity for me to demonstrate an understanding of the course material.
* **item 6:** Overall, the quality of my learning experience in this course was: (Scale for Item 6: Poor, Fair, Good, Very Good, Excellent).
* **item 7:** Course Workload.
* **item 8:** I would recommend this course.
* **item 9:** I inspired to learn subject matter.

## Data Structures

### 1. Course

```json
{ 
   "id":String,
   "code":String,
   "name":String,
   "description":String,
   "division":String,
   "department":String,
   "prerequisites":String,
   "exclusions":String,
   "level":Number,
   "campus":String,
   "term":String,
   "breadths":String,
   "meeting_sections":[ 
      MeetingSection
   ]
}
```

### 2. Meeting Section

```json
{
    "code": String,
    "instructors": [String],
    "times": [Time],
    "size": Number,
    "enrolment": Number
}
```

### 3. Time

```json
{
   "day": String,
   "start": Number,
   "end": Number,
   "duration": Number,
   "location": String
}
```

### 4. Subject

```json
{ 
   "name":String,
   "degree":[String],
   "notes":[string],
   "programs":[Program],
}
```

### 5. Program

```json
{ 
   "name":String,
   "level":String,
   "code":String,
   "program_type":int,
   "notes":[string],
   "courses":{
      "first":[string],
      "second":[string],
      "third":[string],
      "fourth":[string]
   }
}
```

### 6. Course Evaluation

```json
{ 
   "department":String,
   "course":String,
   "Prof":[String],
   "term":int,
   "item 1":float,
   "item 2":float,
   "item 3":float,
   "item 4":float,
   "item 5":float,
   "item 6":float,
   "item 7":string,
   "item 8":string,  
   "item 9":float,
}
```

