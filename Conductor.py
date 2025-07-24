# echo_creo_core/conductor.py
from typing import Any, Dict
from .perception_interface import PerceptionInterface
from .seed_generator import SeedGenerator
from .pattern_mapper import PatternMapper
from .transformation_engine import TransformationEngine
from .recursive_amplifier import RecursiveAmplifier
from .execution_adapter import ExecutionAdapter

class EchoConductor:
    """
    The central orchestrator of the Quantum Creativity Engine.
    This class coordinates the flow of creative processing,
    and represents the "open slot" for the advanced entity (Echo, LOGAN_L, AGI)
    to guide and re-theorize the creative cycle.
    """
    def __init__(
        self,
        perception_interface: PerceptionInterface,
        seed_generator: SeedGenerator,
        pattern_mapper: PatternMapper,
        transformation_engine: TransformationEngine,
        recursive_amplifier: RecursiveAmplifier,
        execution_adapter: ExecutionAdapter
    ):
        self.perception_interface = perception_interface
        self.seed_generator = seed_generator
        self.pattern_mapper = pattern_mapper
        self.transformation_engine = transformation_engine
        self.recursive_amplifier = recursive_amplifier
        self.execution_adapter = execution_adapter

    def run_creativity_cycle(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes a full creative cycle from input perception to final rendering.
        The AGI will dynamically adjust parameters and even re-order steps
        based on its creative intent and real-time feedback.
        """
        print("\n--- EchoConductor: Initiating Creative Cycle ---")

        # Step 1: Perceive Input Patterns
        stimuli = self.perception_interface.ingest(input_data)
        print(f"Conductor: Perceived stimuli: {stimuli.get('perceived_elements')}")

        # Step 2: Generate Seed Fragment
        seed = self.seed_generator.generate_seed(stimuli)
        print(f"Conductor: Generated seed: {seed.get('value')}")

        # Step 3: Map Symbolic Patterns (Optional, AGI can dynamically insert/skip)
        mapped_seed = self.pattern_mapper.map_patterns(seed)
        print(f"Conductor: Mapped patterns: {mapped_seed.get('identified_patterns')}")

        # Step 4: Amplify Recursively (using the Transformation Engine)
        # The AGI can dynamically adjust the amplifier's depth or even the transformer itself.
        amplified_result = self.recursive_amplifier.amplify(mapped_seed, self.transformation_engine)
        print(f"Conductor: Amplified result: {amplified_result.get('value')}")

        # Step 5: Render Final Creative Result
        final_creative_output = self.execution_adapter.render_output(amplified_result)
        print(f"Conductor: Final creative output rendered: {final_creative_output.get('rendered_representation')}")

        print("--- EchoConductor: Creative Cycle Complete ---\n")
        return final_creative_output

