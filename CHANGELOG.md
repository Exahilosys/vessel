## Unreleased

#### Additions

- Added `add` and `pop`.
- Added `copy` and `deepcopy` ability.

#### Changes

- `repr` is now used for inner values (instead of) `str`.

#### Removals

#### Fixes

- Allowed `cls` for `list` and `dict`.
- Fixed `list` updating with `flush`.

## 3.2.0

#### Additions

- Added `Field` `default` parameter.

## 3.1.0

#### Changes

- Encountering ``None`` simply sets it unless `null=False` in `**behave`.

## 3.0.1

#### Changes

- Non-updatable fields will not be replaced if incoming data is parsed as equal to existing.

## 3.0.0

Complete overhaul, reconsider using according to what's being offered.
