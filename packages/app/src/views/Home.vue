<template>
  <v-container>
    <v-row>
      <v-col>
        <course-search-bar v-if="!$apollo.loading" :courses="formattedCourses" />
        <v-skeleton-loader
        v-else
        class="mx-auto"
        max-width="1200"
        type="list-item"
        ></v-skeleton-loader>
      </v-col>
    </v-row>
    <v-row style="background: #E5E5E5;">
      <v-col>
        <timetable-course-card
          class="my-4"
          v-for="(course, code) in selectedCourses"
          :key="code"
          :course="course"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <optimization-settings />
      </v-col>
    </v-row>
    <v-row style="background: #E5E5E5;">
      <v-col>
        <timetable :timetable="timetable" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CourseSearchBar from "../components/CourseSearchBar";
import Timetable from "../components/Timetable";
import OptimizationSettings from "../components/OptimizationSettings";
import TimetableCourseCard from "../components/TimetableCourseCard";
import COURSES_SEARCH_BAR_QUERY from "../graphql/CoursesSearchBar.gql";
import { mapGetters } from "vuex";
export default {
  components: {
    OptimizationSettings,
    CourseSearchBar,
    Timetable,
    TimetableCourseCard
  },
  computed: {
    ...mapGetters(["selectedCourses", "timetable", "courseCodeColorMap"]),
    formattedCourses() {
      return this.courses.map(course => `${course.code}: ${course.name}`);
    },
  },
  apollo: {
    courses: COURSES_SEARCH_BAR_QUERY
  },
  methods: {
    getFormattedCodeAndName(code, name) {
      return `${code} ${name}`;
    }
  }
};
</script>
