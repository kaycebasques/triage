# 9338

https://github.com/sphinx-doc/sphinx/issues/9338

## Attempted repro

### Clone

```
git clone https://github.com/kaycebasques/triage.git
```

### Change working dir

```
cd triage/sphinx/9338
```

### Build

Linux:

```
../../bazelisk/linux/amd64 run :debug
```

macOS:

```
../../bazelisk/darwin/arm64 run :debug
```

We're looking for a nitpicky error along the lines of
`:py:class reference target not found: _thread.allocate_loc` and
it indeed still repros in Sphinx 9.1:

```
Running Sphinx v9.1.0
loading translations [en]... locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
done
making output directory... done
locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
building [mo]: all of 0 po files
writing output... 
building [html]: all source files
updating environment: locale_dir /usr/local/google/home/kayce/.cache/bazel/_bazel_kayce/d624a0b6c31459f1cbf59a7d644694f4/execroot/_main/bazel-out/k8-fastbuild/bin/docs/docs.run.runfiles/_main/docs/_docs/_sources/locales/en/LC_MESSAGES does not exist
[new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index

looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
copying assets... 
copying static files... 
Writing evaluated template result to /tmp/sphinx-out/_static/language_data.js
Writing evaluated template result to /tmp/sphinx-out/_static/documentation_options.js
Writing evaluated template result to /tmp/sphinx-out/_static/basic.css
Writing evaluated template result to /tmp/sphinx-out/_static/alabaster.css
copying static files: done
copying extra files... 
copying extra files: done
copying assets: done
writing output... [100%] index

<unknown>:1: WARNING: py:class reference target not found: _thread.allocate_lock [ref.class]
generating indices... genindex py-modindex done
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build finished with problems, 1 warning (with warnings treated as errors).
```

### (Optional) Cleanup

If you don't otherwise use Bazel and want to delete what it downloaded,
built, etc. then you just need to delete the following directory. Everything
it does is isolated into this dir. It doesn't mess with your paths or anything
like that.

* Linux

  * `~/.cache/bazel`

* macOS

  * `~/Library/Caches/bazel` (Bazel 9 and newer)

  * `/private/var/tmp/_bazel_$USER` (Bazel 8 and older)

* Windows

  * `%USERPROFILE%\_bazel_%USERNAME%`
