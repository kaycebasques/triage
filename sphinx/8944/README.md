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

Linux:

```
../../bazelisk/linux/amd64 run :preview
```

macOS:

```
../../bazelisk/darwin/arm64 run :preview
```

### 4. View

Go to http://0.0.0.0:8000

`custom_descr` is listed in the API reference for `Foo` class
but there is no way to jump to the source code for the
underlying descriptor `CustomDescriptor` that is defined in
`foo/descriptors.py`

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
  implements `__get__()` in `foo/descriptors.py`

- `foo.Foo.name`: A built-in descriptor created via the `@property` decorator
  in `foo/__init__.py`

Sphinx `autodoc` and `viewcode` document these attributes, but fail to generate
`[source]` links for them.
