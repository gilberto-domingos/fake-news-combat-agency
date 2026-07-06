from entity.drafts.methods_experiment import MethodsExperiment


class MethodsExperimentTest:
    @staticmethod
    def run() -> None:
        variable = MethodsExperiment(
            is_active=False,
            keywords=["homicidio", "sequestro", "assalto"]
        )
        print(f"Activate: {variable.is_active}")
        print(f"Keywords: {variable.keywords} ")

        try:
            variable.activate()
            print(f"Status after activate(): {variable.is_active}")

            variable.deactivate()
            print(f"Status after deactivate(): {variable.is_active}")


        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    MethodsExperimentTest.run()
