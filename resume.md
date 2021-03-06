title: Résumé: Heungsub Lee

Heungsub Lee
============

Contact {: .label }
: [heungsub@subl.ee](mailto:heungsub@subl.ee)
  or
  [+82 10-3215-2380](sms:821032152380)
  {: .attr }

Web Sites {: .label }
: [subl.ee](/),
  [github.com/sublee](https://github.com/sublee),
  [linkedin.com/in/sublee](https://linkedin.com/in/sublee)
  {: .attr }

---

Interests
---------

- Back-end engineering for ML projects
- Developing and documenting API for engineers or researchers
- Free and open-source software

Skills
------

Programming Languages {: .label }
: Python (expert), Go, Bash, C#, JavaScript
  {: .attr }

AI Research {: .label }
: PyTorch, Triton Inference Server, NVIDIA Nsight Systems, pipeline parallelism
  {: .attr }

Back-end Development {: .label }
: Linux, AWS, Terraform, Docker, ZeroMQ, Redis, Couchbase, MySQL, etcd
  {: .attr }

---

Work Experience
---------------

Software Engineer {: .label }
[Naver][], 2020--
:   A technology company.
    {: .note }

:   Work for [Clova][]. Just joined.

Software Engineer {: .label }
[Kakao Brain][kakaobrain], 2018--2020
:   The AI research lab in Kakao.
    {: .note }

:   Developed [torchgpipe][] which reproduces [GPipe][] in PyTorch to boost the
    training performance of large deep learning models.

    Developed a serverless training framework and a distributed hyperparameter
    search platform for AutoML.

[clova]: https://clova.ai/
[naver]: https://navercorp.com/en
[kakaobrain]: https://kakaobrain.com/
[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965

Game Server Engineer & Architect {: .label }
[Nexon][], 2011--2018
:   Developed and launched Durango, [KartRider][] Dash & Coin Rush.
    {: .note }

:   Designed and developed cloud-based distributed game servers for Durango
    (MMORPG) and [KartRider][] Dash & Coin Rush (online racing games)
    respectively. Durango achieved up to 70k concurrent users per game world.

    Developed an internationalization and localization system focused on
    linguistic features of Korean and Indo-European languages.

    Researched rating systems such as Elo, Glicko, and
    [TrueSkill][trueskill-tm] to develop a matchmaker.

    Managed a server engineering team including 15 engineers.

[nexon]: https://company.nexon.com/eng
[kartrider]: http://kart.nexon.com/
[trueskill-tm]: http://research.microsoft.com/en-us/projects/trueskill/

Web Developer {: .label }
[Npine][], 2008--2011
:   Supplies stock images for business on [Iclickart][].
    {: .note }

:   Developed and maintained web services from scratch. Maintained on-premise
    Linux servers.

[npine]: http://en.npine.com/
[iclickart]: http://iclickart.co.kr/

Front-end Web Developer {: .label }
[Lunant][], 2008--2011
:   Served social media named VLAAH.
    {: .note }

:   Designed and implemented the UI/UX for social media.

    Developed [jDoctest][] which is an open-source JavaScript testing framework
    inspired by Python's doctest.

[lunant]: http://lunant.net/
[jdoctest]: https://lunant.github.com/jdoctest

Open Source Experience
----------------------

[torchgpipe][], 2019--2020
:   A GPipe implementation in PyTorch.
    {: .note }

:   Implemented [GPipe][] in PyTorch. GPipe is a scalable pipeline parallelism
    library for the training of a giant model. The story behind this project
    can be found on [Kakao Brain Blog<sup>ko</sup>][torchgpipe-blog].

    Optimized the pipeline parallelism and checkpointing for CUDA and PyTorch's
    autograd engine.

[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965
[torchgpipe-blog]: https://kakaobrain.com/blog/66

[Hangulize][], 2010--
:   Automatically transcribes a non-Korean word into Hangul.
    {: .note }

:   Implemented an automatic Hangul transcription algorithm to realize [Brian
    Jongseong Park's idea][hangulize-idea]. By origin, it was written in
    Python, but rewritten in Go for better features, performance, and
    productivity.

    Designed and implemented the web service and RESTful API. Many professional
    Korean translators habitually visit here to translate undocumented proper
    nouns. For example, Ryu Gwang, who is a technical translator, introduced
    Hangulize in [his posting<sup>ko</sup>][ryugwang]. Netflix also refers to
    it in [the Korean timed text style guide][netflix-style].

[hangulize]: https://hangulize.org/
[hangulize-idea]: http://iceager.egloos.com/2610028
[ryugwang]: http://occamsrazr.net/tt/351
[netflix-style]: https://partnerhelp.netflixstudios.com/hc/en-us/articles/216001127-Korean-Timed-Text-Style-Guide

[TrueSkill][trueskill], 2012--
:   A TrueSkill™ implementation in Python.
    {: .note }

:   Implemented [TrueSkill™][trueskill-tm], which is a rating algorithm for
    Xbox Live, in Python with a handy interface. This project was introduced in
    [PyData Berlin 2019][pydata2019].

[trueskill]: https://trueskill.org/
[trueskill-tm]: http://research.microsoft.com/en-us/projects/trueskill/
[pydata2019]: https://docs.google.com/presentation/d/1S5v9D31vpsr22efMSSCO6hmN2SQNCIqKG7JyGzUSzeI/edit?usp=sharing

[Profiling][], 2014--2018
:   An interactive profiler for Python inspired by the Unity3D profiler.
    {: .note }

:   Developed a Python profiler with an interactive TUI inspired by [the Unity
    profiler][unity-profiler].

    On GitHub, this project has been starred by 3k people. Also, it was the 3rd
    daily trending repository on Sep 22, 2014.

[profiling]: https://github.com/what-studio/profiling
[unity-profiler]: https://docs.unity3d.com/Manual/ProfilerWindow.html

Others
:   - [Tossi][] -- A utility for Korean allomorphic particles.
    - [Flask-AutoIndex][] -- mod_autoindex for [Flask][].
    - [SUBLEERUNKER][] -- A simple parody game of SUBERUNKER. Play it in your
                          web browser.
    - [Me2virus][] -- An XSS attack on social media named [Me2day][]. When a
                      user looks at an infected post, a new infected post was
                      written on the user's wall.

[tossi]: https://github.com/what-studio/tossi
[flask-autoindex]: http://pythonhosted.org/Flask-AutoIndex
[flask]: https://flask.palletsprojects.com/
[subleerunker]: /runker/
[me2virus]: https://github.com/sublee/me2virus
[me2day]: https://en.wikipedia.org/wiki/Me2day

Contributions
:   - For [PyTorch][],
      fixed potential GPU memory violation ([#27371][pytorch#27371]);
      deprecated inconsistent API ([#21006][pytorch#21006],
      [#25985][pytorch#25985]); discussed a counterintuitive behavior
      of the autograd engine ([#18568][pytorch#18568]).
    - For [ZeroMQ][],
      discussed a PUB socket crash ([#2942][zeromq#2942]).
    - For [Flask][],
      fixed a bug to generate URL with a subdomain ([#108][flask#108]).
    - For [jQuery 1.4.3][jquery-143],
      restored a missing part of the content negotiation header for Ajax.

[pytorch]:       https://pytorch.org/
[pytorch#27371]: https://github.com/pytorch/pytorch/pull/27371
[pytorch#21006]: https://github.com/pytorch/pytorch/pull/21006
[pytorch#25985]: https://github.com/pytorch/pytorch/pull/25985
[pytorch#18568]: https://github.com/pytorch/pytorch/pull/18568
[zeromq]:        http://zeromq.org/
[zeromq#2942]:   https://github.com/zeromq/libzmq/issues/2942
[flask]:         https://flask.palletsprojects.com/
[flask#108]:     https://github.com/pallets/flask/issues/108
[jquery-143]:    https://blog.jquery.com/2010/10/16/jquery-143-released/

Publications
------------

- C. Kim\*, _H. Lee_\*, M. Jeong, W. Baek, B. Yoon, I. Kim, S. Lim, S. Kim.
  "torchgpipe: On-the-fly Pipeline Parallelism for Training Giant Models".
  [arXiv preprint arXiv:2004.09910][arxiv:torchgpipe]. (2020)

*[C. Kim]:   Chiheon Kim
*[H. Lee]:   Heungsub Lee
*[M. Jeong]: Myungryong Jeong
*[W. Baek]:  Woonhyuk Baek
*[B. Yoon]:  Boogeon Yoon
*[I. Kim]:   Ildoo Kim
*[S. Lim]:   Sungbin Lim
*[S. Kim]:   Sungwoong Kim

[arxiv:torchgpipe]: https://arxiv.org/abs/2004.09910

\*Contributed equally.
{: .footnote }

Public Speeches
---------------

- [Remake of Hangulize<sup>ko</sup>][gokr1808] at Golang Korea 2018 and Naver D2
- [Server architecture of Durango Vol. 3<sup>ko</sup>][ndc18] at NDC 2018
- [Python Survival Guide<sup>ko</sup>][nxtk16] at Nexon Talk 2016
- [Server architecture of Durango Vol. 2<sup>ko</sup>][ndc16] at NDC 2016
- [Profiling<sup>ko</sup>][pycon15] at PyCon KR 2015
- [Server architecture of Durango<sup>ko</sup>][ndc14] at NDC 2014

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

[gokr1808]: https://subl.ee/~gokr1808
[nxtk16]:   https://subl.ee/~nxtk16
[pycon15]:  https://subl.ee/~pycon15

---

Languages
---------

- Korean -- native
- English -- conversational

Education
---------

Computer Software, [Kwangwoon University][kw], 2008
-- Completed the first year only.

[kw]: http://www.kw.ac.kr/

<!-- abbrs -->
*[AWS]: Amazon Web Services
*[CLI]: Command-line interface
*[ML]:  Machine learning
*[MMORPG]: Massively multiplayer online role-playing game
*[NDC]: Nexon Developers Conference
*[TUI]: Text-based user interface
*[XSS]: Cross-site scripting
