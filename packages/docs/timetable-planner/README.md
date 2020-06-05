# Timetable Planner

A web app that helps UofT students plan their courses to generate their optimal timetable. 

The timetable planner allows students to enter their course load and get back a timetable that fits their needs. The vision for the timetable planner includes taking student preferences into account such as: 

- How early students wish to start and end classes
- What days students would like to take off
- What times students would prefer gap time and breaks


## Overview

![timetable-journey](./Timetable-journey.png)

Once the user selects the courses from the Course Guide:

![coursechosing](./coursechosing.png)

The user views the timetable:

The timetable will display whether or not if the selected courses have a valid time, that is no conflict for all courses.

 - Valid:
 
![timetable](./timetable.png)

 - Invalid:
 
![error1](./error1.png)

There are serveral preferences that the user can select to optimize the timetable:

![timetableconstraint](./timetableconstraint.png)


 - Minimize/Maximize idle time: The user can maximize or minimize the gap time between courses.
 - Days off: The user can select the day(s) off so there will be no course appear on that day.
 - Avoid Morning/Evening Class: The user can choose whether if they want to have courses in the morning or evening.
 
The timetable will return invalid and displays a message if the constraints are unreachable.

![error2](./error2.png)

The user can also choose to lock certain course times. 

When preferences are made, those times will not be changed.

![lock1](./lock1.png)

after some preferences made:

![lock2](./lock2.png)


## Example Usage:

### Future Implementation:

<details>
<summary>Pseudocodes</summary>
<details>
<summary> Parse from course name to individual section</summary>

```json

This program takes in the input data from below and output all combinations of the section times of the courses.

function courseToTime(dic_courses){

    for course in dic_courses
        for section in the course
            check if the enrolment is not full
                Add to the list of available for that course
    Make a combination out of all the courses
    return a list of all possible combination

}

```

</details>

<details>
<summary> Idle Time</summary>

```json

This program takes in a set of timetables and outputs the desired timetable based on the preference

function idleTime(set_timetable, max_or_min){

    for timetable in set_timetable
        sum up all the idletime and store the idex
    check for the max and min of the idletimes
    return based on max_or_min

}

```

</details>
</details>


Given a set of course codes, the timetable planner outputs the schedule available for the set.

If no such schedule available, outputs "inValid".

//Setting up preference are still work in progress

#### Input:

1. At the beginning, user inputs the selected courses:


<details>
    <summary>Input Data</summary>

```json
#provided two courses with two section for simplicity
{
    "CourseCode": {
        "CSC108H5F2019":{
            "L0101":[{
                "MONDAY":[32400, 36000],
                "WEDNESDAY":[32400, 36000],
                "FRIDAY":[32400, 36000],
                "size":160,
                "enrolment":0

            }],
            "L0107":[{
                "WEDNESDAY":[64800, 75600],
                "size":160,
                "enrolment":0
                }]
        },
        "CSC318H5F2019":{
            "L0101":[{
                "TUESDAY":[68400, 75600],
                "WEDNESDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
            }],
            "T0107":[{
                "THURSDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
                }]
        },
        
}

```

</details>


<details>
    <summary>Output Data</summary>

#### Output:

```json

{
    "MONDAY":[
        {
            "CSC108H5F2019L0101":[32400, 36000]
        }
        ],
    "TUESDAY":[
        {
            "CSC318H5F2019L0101":[68400, 75600]
        }
        ],
    "WEDNESDAY":[
        {
            "CSC108H5F2019L0101":[32400, 36000]
        },
        {
            "CSC318H5F2019L0101":[68400, 75600]
        }
        ],
    "THURSDAY":[
        {
            "CSC318H5F2019T0101":[68400, 75600]
        }
        ],
    "FRIDAY":[
        {
            "CSC108H5F2019L0101":[32400, 36000]
        }
        ],
}

```

</details>

2. In TimetablePlanner, user inputs the preferrences:

<details>
<summary>Constraint days</summary>

Valid:

<details>
    <summary>Input Data</summary>

```json
#provided two courses with two section for simplicity
{
    "CourseCode": {
        "CSC108H5F2019":{
            "L0101":[{
                "MONDAY":[32400, 36000],
                "WEDNESDAY":[32400, 36000],
                "FRIDAY":[32400, 36000],
                "size":160,
                "enrolment":0

            }],
            "L0107":[{
                "WEDNESDAY":[64800, 75600],
                "size":160,
                "enrolment":0
                }]
        },
        "CSC318H5F2019":{
            "L0101":[{
                "TUESDAY":[68400, 75600],
                "WEDNESDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
            }],
            "T0107":[{
                "THURSDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
                }]
        },
        "Constraints":{
            "INVALIDTIME":[{
                "FRIDAY":[0, 1000000],//Friday off
                "WEDNESDAY":[75600, 1000000],// Wednesday avoiding evening class
            }]
        }
        
}

```

</details>

<details>
    <summary>Output Data</summary>

#### Output:

```json

{
    "MONDAY":[
        {

        }
        ],
    "TUESDAY":[
        {
            "CSC318H5F2019L0101":[68400, 75600]
        }
        ],
    "WEDNESDAY":[
        {
            "CSC108H5F2019L0107":[68400, 75600]
        },
        {
            "CSC318H5F2019L0101":[68400, 75600]
        }
        ],
    "THURSDAY":[
        {
            "CSC318H5F2019T0101":[68400, 75600]
        }
        ],
    "FRIDAY":[
        {

        }
        ],
}

```

</details>


Invalid:

<details>
    <summary>Input Data</summary>

```json
#provided two courses with two section for simplicity
{
    "CourseCode": {
        "CSC108H5F2019":{
            "L0101":[{
                "MONDAY":[32400, 36000],
                "WEDNESDAY":[32400, 36000],
                "FRIDAY":[32400, 36000],
                "size":160,
                "enrolment":0

            }],
            "L0107":[{
                "WEDNESDAY":[64800, 75600],
                "size":160,
                "enrolment":0
                }]
        },
        "CSC318H5F2019":{
            "L0101":[{
                "TUESDAY":[68400, 75600],
                "WEDNESDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
            }],
            "T0107":[{
                "THURSDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
                }]
        },
        "Constraints":{
            "INVALIDTIME":[{
                "TUESDAY":[0, 1000000],//Tuesday off
                "WEDNESDAY":[75600, 1000000],// Wednesday avoiding evening class
            }]
        }
        
}

```

</details>

<details>
    <summary>Output Data</summary>

#### Output:

```json

"invalid"//There are courses at Tuesday

```

</details>
</details>

## Current Implementateion
### (WIP)

<details>
<summary>Pseudocodes</summary>
<details>
<summary> Check Conflict</summary>

```json

This program checks if there are conflict in the timetable

function overlap (dic_timetable){

    for time in timetable
        if the time overlaps each other
            return invalid
    return valid

}

```

</details>
<details>
<summary> Tansform course sections to timetable</summary>

```json

This program transform specific course secitons to a timetable

funtion transform(dic_course){

    for course in dic_course
        append to timetable
    check if valid or not by overlap function

}

```

</details>
</details>


Given a set of times, check if there is a valid timetable avaliable.

Outputs "Valid" if such timetable exist, or else "inValid".

<details>
<summary>Input</summary>

```json
#provided one set of time to check if a valid timetable exist
{
    "CourseCode": {
        "CSC108H5F2019":{
            "L0101":[{
                "MONDAY":[32400, 36000],
                "WEDNESDAY":[32400, 36000],
                "FRIDAY":[32400, 36000],
                "size":160,
                "enrolment":0

            }],
        },
        "CSC318H5F2019":{
            "L0101":[{
                "TUESDAY":[68400, 75600],
                "WEDNESDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
            }],
        },
        
}
```

</details>


<details>
<summary>Output</summary>

```json
"Valid"
```

</details>

### or


<details>
<summary>Input</summary>

```json
#provided one set of time to check if a valid timetable exist
{
    "CourseCode": {
        "CSC108H5F2019":{
            "L0107":[{
                "WEDNESDAY":[64800, 75600],
                "size":160,
                "enrolment":0
                }]
        },
        "CSC318H5F2019":{
            "L0101":[{
                "TUESDAY":[68400, 75600],
                "WEDNESDAY":[68400, 75600],
                "size": 60,
                "enrolment": 0
            }],
        },
        
}

```

</details>

<details>
<summary>Output</summary>

```json

"inValid"
```
</details>
