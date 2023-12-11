RuntimeWarning: 'nltk.downloader' found in sys.modules after import of package 'nltk', but prior to execution of 'nltk.downloader'; this may result in unpredictable behaviour | https://www.google.com/search?q=RuntimeWarning%3A+%27nltk.downloader%27+found+in+sys.modules+after+import+of+package+%27nltk%27%2C+but+prior+to+execution+of+%27nltk.downloader%27%3B+this+may+result+in+unpredictable+behaviour&rlz=1C1YTUH_enIE1084IE1084&oq=RuntimeWarning%3A+%27nltk.downloader%27+found+in+sys.modules+after+import+of+package+%27nltk%27%2C+but+prior+to+execution+of+%27nltk.downloader%27%3B+this+may+result+in+unpredictable+behaviour&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg60gEHNTUyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

____

RuntimeWarning: 'nltk.downloader' found in sys.modules after import of package 'nltk', but prior to execution of 'nltk.downloader'

Issue is reported in nltk-github
https://stackoverflow.com/questions/54412655/runtimewarning-nltk-downloader-found-in-sys-modules-after-import-of-package

____

RUN python -c "import nltk; nltk.download('popular')" | Runtime warning when using nltk.downloader from CLI #2162 | GitHub | https://github.com/nltk/nltk/issues/2162

____

Reproduce error:

```bash
python -m nltk.downloader popular
```

Fix:

```bash
python -c "import nltk; nltk.download('popular')"
```