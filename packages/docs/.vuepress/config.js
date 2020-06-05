module.exports = {
    title: "UofT Course Tools",
    description:
        "We're unifying UofT's course data, and using it to build tools such as a course guide and timetable planner.",
    themeConfig: {
        logo: "/logo.png",
        repo: "utm-hacklab/uoftcoursetools",
        editLinks: true,
        editLinkText: "Edit on Github!",
        lastUpdated: "Last Updated",
        nav: [
            { text: "Home", link: "/" },
            { text: "Course API", link: "/course-api/" },
            { text: "Timetable Planner", link: "/timetable-planner/" },
            { text: "Course Guide", link: "/course-guide/" },
            { text: "Application", link: "https://uoftplanner.netlify.app" },
        ],
    },
    dest: "./docs",
};
