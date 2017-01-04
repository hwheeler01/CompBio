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
      <td><a class="reference internal" href="#repos">GitHub Repo Checks</a></td>
    </tr>
    <tr>
	<td><a class="reference external" href="#code">Project Code</a></td>
      <td><a class="reference external" href="#note">Application Note</a></td>
    </tr>
  </tbody>
</table>

<span style="font-weight: bold;"><a name="rosalind"></a></span>

## ROSALIND

ROSALIND, named after superstar scientist <a href="https://en.wikipedia.org/wiki/Rosalind_Franklin">Rosalind Franklin</a>, is a platform for learning bioinformatics and programming through problem solving. We will be using it in COMP 383 to introduce Python and to practice solving computational problems relevant to molecular biology.

The first 4 assignments in the course will be submitted via the ROSALIND interface. To enroll, click
<a href="http://rosalind.info/classes/enroll/ae1cc7502c/">here</a>.

Once you are enrolled, you will see the assigment problems listed <a href="http://rosalind.info/classes/382/">here</a>. Each problem is due by 2:45 PM on the date listed (also see the <a href="http://hwheeler01.github.io/CompBio/syllabus/#schedule">course schedule</a>). You will be required to upload your commented code with your solution to each problem. Your code must be commented in **your own words** and turned in independently. Code should be commented sufficiently so someone learning Python can understand it. If you don't comment your code, you can only get a maximum of half credit for each assignment. If you work together with someone in class, make sure your code and comments are your own. Do not cut and paste others' work. Cheating includes submitting as your own work something that has been written by another person and/or found on a web site. You may be asked questions about how your code works and your comments will help you explain. Inability to answer such questions will result in a reduced grade.
<span style="font-weight: bold;"><a name="parser"></a></span>

## Python Parser

For better or worse, new file formats are developed frequently in computational biology, often <a href="https://www.biostars.org/p/55351/">every time</a> a new method or software is released. Thus, as budding computational biologists, you will often be tasked with converting files from one format to another in order to try out a shiny new method on your data. If you're lucky, someone will have written and posted a script to do exactly what you want. Often, however, it is quicker/safer/easier to write your own script. For this assignment, you will be given the "real life" task of coverting imputed genotype data into a format appropriate for a new method. Details are <a href="http://hwheeler01.github.io/CompBio/vcf_parser.html">here</a>. 

<span style="font-weight: bold;"><a name="present"></a></span>

## Group Presentations

You will be involved in four group presentations over the course of the semester. All members of the group must contribute to the development of the presentation. Each presentation will be followed by a question and answer period; all members should contribute to addressing the questions. If you've already spoken, let someone else answer first. If you haven't yet spoken, speak up. **Presentation files are due via <a href="https://sakai.luc.edu/">Sakai</a> prior to the start of class on the day of the presentation.** Slides should be clear, straight-forward, and concise. Uploaded slides should be in either `.pptx` or `.pdf` format.
- **Initial Group Presentation of Project (10 pts):** This presentation will be 20-25 minutes in length with 5 minutes for questions. The group will present to the entire class the problem they will aim to solve. This requires digging through the literature to present the background and motivation as well as the “current state” of things for the problem. This presentation must also discuss the language(s) and software that will be used for development and an outline of the key benchmarks that will be met each week throughout the remainder of the semester. More details <a href="http://hwheeler01.github.io/CompBio/init_pres.html">here</a>.- **5-minute Group Progress Presentations (5pts each, 2 presentations total):** As the name implies this will be a quick presentation with two functions: 1) bring the class up to speed on the progress that has been made and 2) introduce any challenges impeding progress. This presentation should include the benchmarks presented initially and discuss how the project is progressing.- **Final Group Presentation (10 pts):** This presentation will be 12 minutes in length with 3 minutes for questions. This is the standard time allotted to oral presentations at a conference. In the presentation, you will present the background, methods, results, and conclusions/future directions. The key to this presentation is being concise and clear. **You should assume you are speaking to a conference audience where most of your audience has not heard about your project before.** You should be shooting for 12 minutes on the nose which gives time for a question or two. Questions can actually help your presentation by clarifying things you perhaps did not present clearly. At 15 minutes all presentations/questions will be stopped. (This is what they really do at a conference.) <a href="http://hwheeler01.github.io/CompBio/final_pres_rubric.html">Grading rubric</a>

<span style="font-weight: bold;"><a name="repos"></a></span>

## GitHub Repo Checks

There will be four due dates for GitHub Repo Checks, 3 points each. In addition to managing your code, your group's GitHub Repository (Repo) will serve as your “research notebook”, tracking your progress throughout the semester. By the end of class time on each day a Repo Check is due make sure all your latest code has been pushed to your repo and that you have recorded notes about what you have done and what you plan to do next. Use the Wiki tab for your progess notes. To earn the full 3 points, each person in the group must have contributed to the repo since the last repo check. This is easily checked by me because I will fork each repo and receive time stamped notifications when you contribute. Contributions include code additions/updates, pull requests, issues discussions, and wiki editing documenting your progress. Make sure the primary repo owner resolves any pull requests made by other group members. Suggestions for organizing your repo are [here](http://hwheeler01.github.io/CompBio/github/#gitsuggest).

<span style="font-weight: bold;"><a name="code"></a></span>

## Project Code

Commented code is due on the day of the scheduled final exam period by 11:59PM. This code should be hosted online through <a href="https://github.com/">GitHub</a>. You should include straight-forward documentation and sample data in your repository. The code should have adequate documentation in the repository's `README.md` file such that anyone could download the code, install it or get it to run, and run through the sample/test data without encountering any problems; this should be thought of as a User’s Manual. **If I cannot run the code and run the test data, I cannot grade the functionality of the code. The breakdown of your group grade for code is: 2 pts comments; 2 pts documentation; 1 pt test data; 10 pts functionality.** Examples of nice `README.md` files with useful documentation and examples can be found <a href="https://github.com/hakyimlab/PrediXcan/tree/master/Software">here</a> and <a href="https://github.com/fcocjin/ReddyMicroRNA">here</a>.

<span style="font-weight: bold;"><a name="note"></a></span>

## Application Note

Parallel to the code developed, you will also be drafting what is commonly referred to as an *Application Note*. This is a brief (2-page journal style, 1000-1300 words plus one image) paper describing the application. It includes Abstract, Background, Implementation, Results, and References sections. The Abstract should be brief (100-200 words). The Background section should introduce the problem as well as the existing software tools that are available to solve the problem, a subset of the problem, or a closely related problem. The Implementation will include details about the development of the application in ENGLISH. In other words, what functionality was developed (not a list of classes/functions); this includes the run-time and memory usage estimates. The Results section typically includes the actual use of your software on a set of data (i.e. your test data) to show how it solves the problem at hand. Likewise, the same set of data is then analyzed by OTHER available tools or statistical models in an effort to show how your solution is superior.You will have two group grades for the Application Note: a **Rough Draft (5 pts)** and the **Final Draft (10 pts)**. The Rough Draft, due 2 weeks prior to the final paper, will provide you with the opportunity to get feedback on your paper. Turn both these assignments in by 11:59PM on their respective due dates via <a href="https://sakai.luc.edu/">Sakai</a>. Be sure the Application Note includes a link to your Project Code <a href="https://github.com/">GitHub</a> repository.