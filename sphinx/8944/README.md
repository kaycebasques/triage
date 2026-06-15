# 8944

https://github.com/sphinx-doc/sphinx/issues/8944

## Repro

### Clone

```
git clone https://github.com/kaycebasques/triage.git
```

### Change working dir

```
cd triage/sphinx/8944
```

### Build & serve

```
<bzl> run //src:serve
```

Replacing `<bzl>` with one of the following:

* linux x86-64: `../../bazelisk/linux/amd64`

* macOS Apple Silicon: `../../bazelisk/darwin/arm64`

### View

Go to http://0.0.0.0:8000

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
