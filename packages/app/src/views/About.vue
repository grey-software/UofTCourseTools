<template>
    <v-app>
        <v-content
            :style="
                darkMode ? 'background-color: #000000' : 'background-color: #F5F5F6'
            "
            class="pt-0"
        >
            <v-app-bar
                fixed
                elevation="0"
                dark
                class="pa-0"
                :style="
                    top
                        ? 'background-color: transparent'
                        : 'background-color: #012B5C'
                "
            >
                <v-img
                    src="../assets/VIA-Planner-White.png"
                    :max-width="$isMobile() ? 100 : 130"
                    contain
                    @click="
                        $isMobile()
                            ? (mobileAlert = true)
                            : $router.push({ name: 'home' })
                    "
                    style="cursor: pointer"
                />
                <v-spacer></v-spacer>
                <v-btn
                    text
                    href="https://docs.google.com/forms/d/e/1FAIpQLScmmk0H3_5KVxoa6m74_Uj93dF-2OCUQF-kPXcr9xki8V71oQ/viewform"
                    target="blank"
                >
                    <v-icon left>mdi-text-box-check-outline</v-icon>
                    Survey
                </v-btn>
                <v-btn
                    v-if="!$isMobile()"
                    text
                    href="https://docs.viaplanner.ca/"
                    target="blank"
                >
                    <v-icon left>mdi-file-document</v-icon>
                    Docs
                </v-btn>
                <v-btn
                    text
                    href="https://github.com/UTM-Hacklab/VIAplanner"
                    target="blank"
                >
                    <v-icon left>mdi-github</v-icon>
                    GitHub
                </v-btn>

                <v-chip
                    link
                    href="https://github.com/UTM-Hacklab/VIAplanner/stargazers"
                    label
                    outlined
                    color="white"
                    target="blank"
                    class="mr-3"
                >
                    <v-icon small left>mdi-star</v-icon>
                    <animated-number
                        :value="starCount"
                        :round="true"
                        :duration="1000"
                    />
                </v-chip>
            </v-app-bar>
            <v-container fluid class="pb-0 pt-0">
                <v-snackbar v-model="mobileAlert">
                    Sorry! The mobile view is not ready yet 😢
                    <template v-slot:action="{ attrs }">
                        <v-btn
                            color="pink"
                            text
                            v-bind="attrs"
                            @click="mobileAlert = false"
                        >
                            Close
                        </v-btn>
                    </template>
                </v-snackbar>
                <v-btn
                    fab
                    dark
                    bottom
                    right
                    fixed
                    color="primary"
                    @click="darkMode = !darkMode"
                >
                    <v-icon v-if="darkMode" dark>mdi-brightness-4</v-icon>
                    <v-icon v-else dark>mdi-brightness-6</v-icon>
                </v-btn>
                <v-row>
                    <v-col class="pa-0">
                        <v-img
                            id="top-image"
                            src="../assets/about-background.jpg"
                            :height="windowHeight"
                            :eager="true"
                        >
                            <v-overlay :opacity="darkMode ? 0.15 : 0" z-index="0" />
                            <v-row
                                align="center"
                                justify="center"
                                class="fill-height"
                            >
                                <v-col class="text-center" cols="12">
                                    <h1
                                        class="text-h2 ma-4"
                                        v-intersect="onIntersect"
                                        style="z-index: 1; position: relative; color: white"
                                    >
                                        Course Selection Made Easy
                                    </h1>
                                    <h1
                                        class="text-h5 ma-4"
                                        style="font-weight: 300; color: white"
                                    >
                                        A tool for tailoring your University
                                        timetable based on your programs
                                    </h1>
                                    <v-btn
                                        rounded
                                        color="white"
                                        x-large
                                        outlined
                                        style="text-transform: none; border-width: medium"
                                        class="ma-4"
                                        @click="
                                            $isMobile()
                                                ? (mobileAlert = true)
                                                : $router.push({ name: 'home' })
                                        "
                                    >
                                        Try out the Alpha
                                    </v-btn>
                                    <v-btn
                                        rounded
                                        color="white"
                                        x-large
                                        outlined
                                        style="text-transform: none; border-width: medium"
                                        class="ma-4"
                                        @click="
                                            $vuetify.goTo('#schedule', {
                                                offset: 78,
                                            })
                                        "
                                    >
                                        Release Schedule
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-img>
                    </v-col>
                </v-row>
                <v-card elevation="4" class="mt-4" :dark="darkMode" id="schedule">
                    <v-row justify="center">
                        <v-col class="text-center">
                            <h1 class="ma-3">Release Schedule</h1>
                            <v-timeline
                                :dense="$vuetify.breakpoint.smAndDown"
                                class="ma-3"
                                align-top
                            >
                                <v-timeline-item
                                    color="green lighten-1"
                                    fill-dot
                                    left
                                >
                                    <v-card color="green lighten-1">
                                        <v-card-title color="green lighten-1">
                                            <v-row>
                                                <v-col>
                                                    <h1 class="text-start">
                                                        PreAlpha
                                                    </h1>
                                                </v-col>
                                                <v-icon size="64">
                                                    mdi-notebook
                                                </v-icon>
                                            </v-row>
                                        </v-card-title>
                                        <v-sheet class="pa-5 text-left">
                                            <ul>
                                                <li>
                                                    Generate timetable based on
                                                    selected courses
                                                </li>
                                                <li>
                                                    Switch sections (lecture,
                                                    practical, tutorial)
                                                </li>
                                                <li>Lock courses</li>
                                                <li>Blocks parts of the day</li>
                                                <li>Block entire days</li>
                                                <li>
                                                    Switch semesters (plan for both
                                                    semesters)
                                                </li>
                                            </ul>
                                            <v-btn class="ma-4 start" disabled>
                                                Upgraded to Alpha
                                            </v-btn>
                                        </v-sheet>
                                    </v-card>
                                </v-timeline-item>

                                <v-timeline-item
                                    color="blue lighten-1"
                                    fill-dot
                                    icon="mdi-party-popper"
                                    right
                                    large
                                >
                                    <v-card color="blue lighten-1">
                                        <v-card-title color="blue lighten-1">
                                            <v-row>
                                                <v-col>
                                                    <h1 class="text-start">Alpha</h1>
                                                    <h1
                                                        class="text-start text-subtitle-1"
                                                    >
                                                        Available Now
                                                    </h1>
                                                </v-col>
                                                <v-icon size="64">
                                                    mdi-progress-upload
                                                </v-icon>
                                            </v-row>
                                        </v-card-title>
                                        <v-sheet class="pa-5 text-left">
                                            <ul>
                                                <li>
                                                    Brand new UI!
                                                </li>
                                                <li>
                                                    Course data updated for 2020 -
                                                    2021 school year (UTM)
                                                </li>
                                                <li>
                                                    Courses now show their delivery
                                                    methods
                                                </li>
                                                <li>
                                                    Export timetable as png
                                                </li>
                                                <li>Horizontal lock</li>
                                                <li>Bug fixes</li>
                                            </ul>
                                            <v-btn
                                                class="ma-4 start"
                                                color="blue lighten-1"
                                                dark
                                                @click="
                                                    $isMobile()
                                                        ? (mobileAlert = true)
                                                        : $router.push({
                                                              name: 'home',
                                                          })
                                                "
                                            >
                                                Try it Now
                                            </v-btn>
                                        </v-sheet>
                                    </v-card>
                                </v-timeline-item>

                                <v-timeline-item color="red lighten-1" fill-dot left>
                                    <v-card color="red lighten-1">
                                        <v-card-title class="red lighten-1">
                                            <v-row>
                                                <v-col>
                                                    <h1 class="text-start">Beta</h1>
                                                    <h1
                                                        class="text-start text-subtitle-1"
                                                    >
                                                        End of August
                                                    </h1>
                                                </v-col>
                                                <v-icon size="64">
                                                    mdi-nuke
                                                </v-icon>
                                            </v-row>
                                        </v-card-title>
                                        <v-sheet class="pa-5 text-left">
                                            <ul>
                                                <li>
                                                    Course suggestion based on
                                                    programs (only for selected
                                                    programs)
                                                </li>
                                                <li>
                                                    Added courses from all 3 campuses
                                                </li>
                                                <li>Bird course recommendations</li>
                                                <li>
                                                    Save timetable in the browser for
                                                    when you visit again
                                                </li>
                                                <li>
                                                    More UI improvement
                                                </li>
                                                <li>
                                                    Work flawlessly with
                                                    self-conflicting courses
                                                </li>
                                                <li>Bug fixes</li>
                                            </ul>
                                            <v-btn
                                                class="ma-4 start"
                                                color="red lighten-1"
                                                disabled
                                            >
                                                Coming Soon
                                            </v-btn>
                                        </v-sheet>
                                    </v-card>
                                </v-timeline-item>
                            </v-timeline>
                            <h1 class="text-body-1 ma-1">
                                Keep in mind, the deadlines for each release is when
                                <strong>ALL</strong> the features will be ready. So
                                come back frequently to check if a new feature has
                                been released 😀
                            </h1>
                        </v-col>
                    </v-row>
                </v-card>
                <v-card elevation="4" class="mt-4" :dark="darkMode">
                    <v-row justify="center">
                        <v-col cols="11" lg="5" order="2" order-lg="1">
                            <v-row
                                align="center"
                                :justify="$isMobile() ? 'center' : 'end'"
                                class="fill-height"
                            >
                                <div
                                    :style="
                                        $isMobile()
                                            ? 'text-align: center'
                                            : 'text-align: right'
                                    "
                                >
                                    <h3>Generate</h3>
                                    <h1 style="margin-bottom: 20px">
                                        Schedule Automatically
                                    </h1>
                                    <h3 class="font-weight-medium">
                                        Simply choose a course
                                    </h3>
                                    <h3
                                        style="margin-bottom: 40px;"
                                        class="font-weight-medium"
                                    >
                                        and we will make a timetable for you
                                    </h3>
                                </div>
                            </v-row>
                        </v-col>
                        <v-col cols="12" lg="7" class="pb-0" order="1" order-lg="2">
                            <div style="text-align:center">
                                <v-img
                                    :class="
                                        $isMobile()
                                            ? ['center', 'ma-3']
                                            : ['center', 'mt-3', 'mb-7', 'mr-5']
                                    "
                                    src="../assets/img1.gif"
                                    max-width="800"
                                    :eager="true"
                                ></v-img>
                            </div>
                        </v-col>
                    </v-row>
                </v-card>
                <v-card elevation="4" class="mt-4" :dark="darkMode">
                    <v-row justify="center">
                        <v-col class="pb-0" cols="12" lg="7">
                            <div style="text-align:center">
                                <v-img
                                    :class="
                                        $isMobile()
                                            ? ['center', 'ma-3']
                                            : ['center', 'mt-3', 'mb-7', 'ml-5']
                                    "
                                    src="../assets/img2.gif"
                                    max-width="800"
                                    :eager="true"
                                ></v-img>
                            </div>
                        </v-col>
                        <v-col cols="11" lg="5" class="pb-0">
                            <v-row
                                align="center"
                                :justify="$isMobile() ? 'center' : 'start'"
                                class="fill-height"
                            >
                                <div
                                    :style="$isMobile() ? 'text-align: center' : ''"
                                >
                                    <h3>Flexibility</h3>
                                    <h1 style="margin-bottom: 20px">
                                        Block Times Off
                                    </h1>
                                    <h3 class="font-weight-medium">
                                        Can't go to school on Tuesdays?
                                    </h3>
                                    <h3
                                        style="margin-bottom: 40px;"
                                        class="font-weight-medium"
                                    >
                                        Just block that day off and we will
                                        reschedule
                                    </h3>
                                </div>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card>
                <v-card elevation="4" class="mt-4" :dark="darkMode">
                    <v-row justify="center">
                        <v-col style="text-align: center">
                            <h1 class="ma-3">Features</h1>
                            <v-carousel
                                show-arrows-on-hover
                                :height="$isMobile() ? 350 : 780"
                            >
                                <v-carousel-item
                                    v-for="(path, text) in slideData"
                                    :key="text"
                                    class="pa-3"
                                    :light="!darkMode"
                                >
                                    <v-sheet>
                                        <v-row>
                                            <v-col>
                                                <p>
                                                    {{ text }}
                                                </p>
                                                <v-img
                                                    class="center"
                                                    :eager="true"
                                                    :src="path"
                                                />
                                            </v-col>
                                        </v-row>
                                    </v-sheet>
                                </v-carousel-item>
                            </v-carousel>
                        </v-col>
                    </v-row>
                </v-card>
                <v-card elevation="4" class="mt-4" :dark="darkMode">
                    <v-row justify="center">
                        <v-col style="text-align: center">
                            <h1 class="ma-3 mb-4">Our Partners</h1>
                            <agile
                                class="ma-3"
                                :slidesToShow="$isMobile() ? 3 : 5"
                                pauseOnHover
                                infinite
                                autoplay
                                :navButtons="false"
                                height="30"
                            >
                                <div>
                                    <v-img
                                        :height="$isMobile() ? 110 : 170"
                                        contain
                                        src="../assets/UTMVSA.png"
                                    ></v-img>
                                </div>
                                <div>
                                    <v-img
                                        :height="$isMobile() ? 110 : 170"
                                        contain
                                          :src="
                                            darkMode
                                                ? require('../assets/WISC-Dark.png')
                                                : require('../assets/WISC-Light.png')
                                        "
                                    ></v-img>
                                </div>
                                <div>
                                    <v-img
                                        :height="$isMobile() ? 110 : 170"
                                        contain
                                        :src="
                                            darkMode
                                                ? require('../assets/UTMSAM-Dark.png')
                                                : require('../assets/UTMSAM-Light.png')
                                        "
                                    ></v-img>
                                </div>
                                <div>
                                    <v-img
                                        :height="$isMobile() ? 110 : 170"
                                        contain
                                        :src="
                                            darkMode
                                                ? require('../assets/DSC-Dark.png')
                                                : require('../assets/DSC-Light.png')
                                        "
                                    ></v-img>
                                </div>
                                <div>
                                    <v-img
                                        :height="$isMobile() ? 110 : 170"
                                        contain
                                        :src="
                                            darkMode
                                                ? require('../assets/UTMEBS-Dark.png')
                                                : require('../assets/UTMEBS-Light.png')
                                        "
                                    ></v-img>
                                </div>
                            </agile>
                        </v-col>
                    </v-row>
                </v-card>
                <v-row
                    justify="center"
                    align="center"
                    :style="$isMobile() ? 'min-height: 500px' : 'min-height: 400px'"
                >
                    <v-col style="text-align: center" cols="12" lg="6">
                        <v-sheet
                            :dark="darkMode"
                            :color="darkMode ? 'black' : '#F5F5F6'"
                        >
                            <h1>Open Source</h1>
                            <h3 class="text-body-1 ma-5">
                                This is a platform built for students, by students.
                                Universities can't always keep up with the
                                <strong>cutting-edge</strong>
                                technologies, but we have made it our mission to do
                                so.
                            </h3>
                            <h3 class="text-body-1">
                                That's why we need your help. At VIAplanner, we are
                                strong believers in <strong>collaboration</strong>.
                                Thus, we've decided to display all of our source
                                code. If you have any ideas that you think would be
                                useful, please don't hesitate to
                                <strong>make it happen.</strong>
                            </h3>
                            <v-row class="mt-5" justify="center">
                                <v-btn
                                    href="https://docs.viaplanner.ca/"
                                    target="blank"
                                    dark
                                    color="#012B5C"
                                    elevation="0"
                                    class="ma-1"
                                >
                                    <v-icon left>mdi-file-document</v-icon>
                                    API Docs
                                </v-btn>
                                <v-btn
                                    href="https://github.com/UTM-Hacklab/VIAplanner"
                                    target="blank"
                                    color="#7C007C"
                                    dark
                                    class="ml-1 mt-1 mb-1"
                                    elevation="0"
                                    style="border-top-right-radius: 0px;border-bottom-right-radius: 0px;"
                                >
                                    <v-icon left>mdi-github</v-icon>
                                    GitHub
                                </v-btn>
                                <v-btn
                                    href="https://github.com/UTM-Hacklab/VIAplanner/stargazers"
                                    target="blank"
                                    color="#670067"
                                    dark
                                    class="mr-1 mt-1 mb-1"
                                    elevation="0"
                                    style="border-top-left-radius: 0px;border-bottom-left-radius: 0px;"
                                >
                                    <v-icon left>mdi-star</v-icon>
                                    {{ starCount }}
                                </v-btn>
                            </v-row>
                        </v-sheet>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
        <v-footer absolute :dark="darkMode" :color="darkMode ? 'black' : '#F5F5F6'">
            <v-row justify="center">
                <h1 class="text-subtitle-1 text-center">
                    Copyright © 2020 VIAplanner - Data updated for the 2020 - 2021
                    school year
                </h1>
            </v-row>
        </v-footer>
    </v-app>
</template>

<script>
import axios from "axios";
import AnimatedNumber from "animated-number-vue";
import { VueAgile } from "vue-agile";

export default {
    components: {
        AnimatedNumber,
        agile: VueAgile,
    },
    data() {
        return {
            top: false,
            starCount: 0,
            slideData: {
                "Generate Timetable: no need to select your own times": require("../assets/slide1.gif"),
                "Switch Sections: complete control over your schedule": require("../assets/slide2.gif"),
                "Block Times: can't go to class during a time? Just block it": require("../assets/slide3.gif"),
                "Lock Sections: lock specific sections and we won't change it": require("../assets/slide4.gif"),
                "Switch Semesters: easily switch between your timetables": require("../assets/slide5.gif"),
                "Export Timetable: export your timetable as png": require("../assets/slide6.gif"),
            },
            mobileAlert: false,
            darkMode: window.matchMedia("(prefers-color-scheme: dark)").matches,
        };
    },
    mounted() {
        axios
            .get("https://api.github.com/repos/UTM-Hacklab/VIAplanner")
            .then((response) => {
                this.starCount = response.data.stargazers_count;
            })
            .catch((error) => {
                console.log(error);
            });
    },
    computed: {
        windowHeight() {
            return window.innerHeight;
        },
    },
    methods: {
        onIntersect(entries) {
            this.top = entries[0].isIntersecting;
        },
    },
};
</script>

<style>
.center {
    margin-left: auto;
    margin-right: auto;
}
</style>
