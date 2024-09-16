import some_module
import some_module.sub_mod


def test_module() -> None:
    assert some_module.sub_mod.NativeClass.__module__ == "some_module.sub_mod"
    assert some_module.sub_mod.CDefClass.__module__ == "some_module.sub_mod"
    assert some_module.NativeClass.__module__ == "some_module"
    assert some_module.CDefClass.__module__ == "some_module"  # fails


if __name__ == "__main__":
    test_module()
