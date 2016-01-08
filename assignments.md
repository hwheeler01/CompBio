---
layout: page
title: Assignments
permalink: /assignments/
---
<table style="width: px; height: 12px;" class="docutils" border="1">
  <caption><b>Index</b></caption> <colgroup><col width="50%"><col width="50%"></colgroup> <tbody valign="top">
    <tr>
      <td><a class="reference internal" href="#rosalind">ROSALIND</a></td>
      <td><a class="reference external" href="#parser">Python Parser</a></td>
    </tr>
    <tr>
      <td><a class="reference external" href="#present">Group Presentations</a></td>
      <td><a class="reference internal" href="#blogs">Blogs</a></td>
    </tr>
    <tr>
	<td><a class="reference external" href="#code">Project Code</a></td>
      <td><a class="reference external" href="#note">Application Note</a></td>
    </tr>
  </tbody>
</table>

<span style="font-weight: bold;"><a name="rosalind"></a></span>
##ROSALIND
ROSALIND, named after superstar scientist <a href="https://en.wikipedia.org/wiki/Rosalind_Franklin">Rosalind Franklin</a>, is a platform for learning bioinformatics and programming through problem solving. We will be using it in COMP 383 to introduce Python and to practice solving computational problems relevant to molecular biology.

The first 4 assignments in the course will be submitted via the ROSALIND interface. To enroll, click
<a href="http://rosalind.info/classes/enroll/f74db871de/">here</a>.

Once you are enrolled, you will see the assigment problems listed <a href="http://rosalind.info/classes/254/">here</a>. Each problem is due by 11:59 PM on the date listed (also see the <a href="http://hwheeler01.github.io/CompBio/syllabus/#schedule">course schedule</a>). You will be required to upload your commented code with your solution to each problem. Your code must be commented in **your own words** and turned in independently. Code should be commented sufficiently so someone learning Python can understand it. **If you had a partner for a problem, note her/his name in your code comments**. Cheating includes submitting as your own work something that has been written by an outside person (or web site). If you are working with a partner, an “outside person” refers to someone other than your partner. 

<span style="font-weight: bold;"><a name="parser"></a></span>
##Python Parser
For better or worse, new file formats are developed frequently in computational biology, often <a href="https://www.biostars.org/p/55351/">every time</a> a new method or software is released. Thus, as budding computational biologists, you will often be tasked with converting files from one format to another in order to try out a shiny new method on your data. If you're lucky, someone will have written and posted a script to do exactly what you want. Often, however, it is quicker/safer/easier to write your own script. For this assignment, you will be given the "real life" task of coverting imputed genotype data into a format appropriate for a new method. Details are <a href="http://hwheeler01.github.io/CompBio/vcf_parser.html">here</a>. 

<span style="font-weight: bold;"><a name="present"></a></span>
##Group Presentations
You will be involved in four group presentations over the course of the semester. All members of the group must contribute to the development of the presentation as well as participate in the actual presentation. Each presentation will be followed by a question and answer period; all members should contribute to addressing the questions. If you've already spoken, let someone else answer first. If you haven't yet spoken, speak up. **Presentation files are due via <a href="https://sakai.luc.edu/">Sakai</a> prior to the start of class on the day of the presentation.** Slides should be clear, straight-forward, and concise. Uploaded slides should be in either `.pptx` or `.pdf` format.
- **Initial Group Presentation of Project (10 pts):** This presentation will be 20-25 minutes in length with 5 minutes for questions. The group will present to the entire class the problem they will aim to solve. This requires digging through the literature to present the background and motivation as well as the “current state” of things for the problem. This presentation must also discuss the language that will be used for development and an outline of the key benchmarks that will be met each week throughout the remainder of the semester.- **5-minute Group Progress Presentations (5pts each, 2 presentations total):** As the name implies this will be a quick presentation with two functions: 1) bring the class up to speed on the progress that has been made and 2) introduce any challenges impeding progress. This presentation should include the benchmarks presented initially and discuss how the project is progressing.- **Final Group Presentation (10 pts):** This presentation will be 12 minutes in length with 3 minutes for questions. This is the standard time allotted to oral presentations at a conference. In the presentation, you will present the background, methods, results, and conclusions/future directions. The key to this presentation is being concise and clear. You should be shooting for 12 minutes on the nose which gives time for a question or two. Questions can actually help your presentation by clarifying things you perhaps did not present clearly. At 15 minutes all presentations/questions will be stopped. (This is what they really do at a conference.) 

<span style="font-weight: bold;"><a name="blogs"></a></span>
##Blogs
There will be four due dates for blog entries, 5 points each. This will serve as your “research notebook”: record what you have done and what you plan to do next. Your blog will be through <a href="https://sakai.luc.edu/">Sakai</a>. Each student will have their ***own*** blog. Each blog itself is worth 2 points. You must also comment on each of your teammate’s blogs (3 points). A few sentences will suffice, but more may be useful. For example, you may want to suggest a different approach to what your teammate has done or plans to do. Your blog is due by 11:59 PM on each Monday indicated on the <a href="http://hwheeler01.github.io/CompBio/syllabus/#schedule">Course Schedule</a>. You must go through and comment on each of your teammate’s blogs (plural) by 11:59 PM on the following Wednesday. Please number each blog entry in the Title: e.g. "Blog 1", "Blog 2", "Blog 3", and "Blog 4."

<span style="font-weight: bold;"><a name="code"></a></span>
##Project Code
Commented code is due on the day of the scheduled final exam period by 11:59PM. This code should be hosted online through <a href="https://github.com/">GitHub</a>. You should include straight-forward documentation and sample data in your repository. The code should have adequate documentation in the repository's `README.md` file such that anyone could download the code, install it or get it to run, and run through the sample/test data without encountering any problems; this should be thought of as a User’s Manual. If I cannot run the code and run the test data, I cannot grade the functionality of the code. The breakdown of your group grade for code is: 2 pts comments; 2 pts documentation; 1 pt test data; 10 pts functionality.

<span style="font-weight: bold;"><a name="note"></a></span>
##Application Note
Parallel to the code developed, you will also be drafting what is commonly referred to as an *Application Note*. This is a brief (2-page journal style, 1000-1300 words plus one image) presentation of the application. It includes Abstract, Background, Implementation, Results, and References sections. The Abstract should be brief (100-200 words). The Background section should introduce the problem as well as the existing software tools that are available to solve the problem, a subset of the problem, or a closely related problem. The Implementation will include details about the development of the application in ENGLISH. In other words, what functionality was developed (not a list of classes/functions); this includes the run-time and memory usage estimates. The Results section typically includes the actual use of your software on a set of data (i.e. your test data) to show how it solves the problem at hand. Likewise, the same set of data is then analyzed by OTHER available tools or statistical models in an effort to show how your solution is superior.You will have two group grades for the Application Note: a **Rough Draft (5 pts)** and the **Final Draft (10 pts)**. The Rough Draft, due 2 weeks prior to the final paper, will provide you with the opportunity to get feedback on your paper. Turn both these assignments in via <a href="https://sakai.luc.edu/">Sakai</a> and be sure the Application Note includes a link to your Project Code repository.