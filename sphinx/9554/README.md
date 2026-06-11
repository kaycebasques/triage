# 9554

https://github.com/sphinx-doc/sphinx/issues/9554

## Repro

### 1. Clone

```
git clone https://github.com/kaycebasques/triage.git
```

### 2. Change working dir

```
cd triage/sphinx/9554
```

### 3. Build & serve

Linux:

```
../../bazelisk/linux/amd64 run :preview
```

macOS:

../../bazelisk/darwin/arm64 run :preview`

### 4. View

Go to http://0.0.0.0:8000

### 5. (Optional) Cleanup

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
