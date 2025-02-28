import importlib
import importlib.util
import pkgutil


def include_all_routers(app, package_name="app.routes"):
    """
    Recursively discover and include all routers in the given package.
    Each module should define a 'router' variable (APIRouter).
    """
    # Import the base package
    package = importlib.import_module(package_name)

    # Iterate over all modules and sub-packages
    for finder, name, is_pkg in pkgutil.iter_modules(package.__path__):
        full_name = f"{package_name}.{name}"
        # Import the module (or sub-package)
        submodule = importlib.import_module(full_name)

        # If it's a package, recurse into it
        if is_pkg:
            include_all_routers(app, full_name)
        else:
            # If there's a 'router' attribute, include it
            if hasattr(submodule, "router"):
                app.include_router(submodule.router)
                print(f"Registered router from {full_name}")
