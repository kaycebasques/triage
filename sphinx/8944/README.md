# 8944

https://github.com/sphinx-doc/sphinx/issues/8944

## Repro

### 1. Clone

```
git clone https://github.com/kaycebasques/triage.git
```

### 2. Change working dir

```
cd triage/sphinx/8944
```

### 3. Build & serve

```
<bzl> run //src:serve
```

Replacing `<bzl>` with one of the following:

* linux x86-64: `../../bazelisk/linux/amd64`

* macOS Apple Silicon: `../../bazelisk/darwin/arm64`

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

## Notes

In Python, a **descriptor** is an attribute whose access behavior is overridden
by implementing the descriptor protocol: `__get__()`, `__set__()`, or
`__delete__()`.

In this reproduction, the descriptors are:
- `foo.Foo.custom_descr`: A custom descriptor whose class `CustomDescriptor`
  implements `__get__()` in
[foo/descriptors.py](file:///usr/local/google/home/kayce/triage/sphinx/8944/foo/descriptors.py).
- `foo.Foo.name`: A built-in descriptor created via the `@property` decorator
  in
[foo/__init__.py](file:///usr/local/google/home/kayce/triage/sphinx/8944/foo/__init__.py).

Sphinx `autodoc` and `viewcode` document these attributes, but fail to generate
`[source]` links for them.
