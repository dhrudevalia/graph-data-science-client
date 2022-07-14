from graphdatascience.graph_data_science import GraphDataScience

# A list of the server endpoints that should not be reachable via the standard
# string builder construction on the `GraphDataScience` class.
# If a new server endpoint is added to pipelines, the test will fail and the
# new endpoint has to be added to this list, as well as to the pipeline classes'
# implementations.
IGNORED_ENDPOINTS = {
    "gds.alpha.graph.graphProperty.drop",  # FIXME: Add support
    "gds.alpha.graph.graphProperty.stream",  # FIXME: Add support
    "gds.beta.graph.relationships.stream",  # FIXME: Add support
    "gds.alpha.pipeline.linkPrediction.addMLP",
    "gds.alpha.pipeline.linkPrediction.addRandomForest",
    "gds.beta.pipeline.linkPrediction.addFeature",
    "gds.beta.pipeline.linkPrediction.addLogisticRegression",
    "gds.beta.pipeline.linkPrediction.addNodeProperty",
    "gds.alpha.pipeline.linkPrediction.configureAutoTuning",
    "gds.beta.pipeline.linkPrediction.configureSplit",
    "gds.beta.pipeline.linkPrediction.predict.mutate",
    "gds.beta.pipeline.linkPrediction.predict.mutate.estimate",
    "gds.beta.pipeline.linkPrediction.predict.stream",
    "gds.beta.pipeline.linkPrediction.predict.stream.estimate",
    "gds.beta.pipeline.linkPrediction.train",
    "gds.beta.pipeline.linkPrediction.train.estimate",
    "gds.alpha.pipeline.nodeClassification.addMLP",
    "gds.alpha.pipeline.nodeClassification.addRandomForest",
    "gds.beta.pipeline.nodeClassification.addLogisticRegression",
    "gds.beta.pipeline.nodeClassification.addNodeProperty",
    "gds.alpha.pipeline.nodeClassification.configureAutoTuning",
    "gds.beta.pipeline.nodeClassification.configureSplit",
    "gds.beta.pipeline.nodeClassification.predict.mutate",
    "gds.beta.pipeline.nodeClassification.predict.mutate.estimate",
    "gds.beta.pipeline.nodeClassification.predict.stream",
    "gds.beta.pipeline.nodeClassification.predict.stream.estimate",
    "gds.beta.pipeline.nodeClassification.predict.write",
    "gds.beta.pipeline.nodeClassification.predict.write.estimate",
    "gds.beta.pipeline.nodeClassification.selectFeatures",
    "gds.beta.pipeline.nodeClassification.train",
    "gds.beta.pipeline.nodeClassification.train.estimate",
    "gds.alpha.pipeline.nodeRegression.addRandomForest",
    "gds.alpha.pipeline.nodeRegression.addLinearRegression",
    "gds.alpha.pipeline.nodeRegression.addNodeProperty",
    "gds.alpha.pipeline.nodeRegression.configureAutoTuning",
    "gds.alpha.pipeline.nodeRegression.configureSplit",
    "gds.alpha.pipeline.nodeRegression.predict.mutate",
    "gds.alpha.pipeline.nodeRegression.predict.stream",
    "gds.alpha.pipeline.nodeRegression.selectFeatures",
    "gds.alpha.pipeline.nodeRegression.train",
    "gds.beta.graph.export.csv.estimate",  # FIXME: Add support
    "gds.util.NaN",
    "gds.util.infinity",
    "gds.util.isFinite",
    "gds.util.isInfinite",
}


def test_coverage(gds: GraphDataScience) -> None:
    result = gds.list()
    for server_endpoint in result["name"].tolist():
        if server_endpoint in IGNORED_ENDPOINTS:
            continue

        # Divide the endpoint string into its parts and cut out the "gds" prefix
        endpoint_components = server_endpoint.split(".")[1:]

        # Check that each step of the string building is a valid object
        base = gds
        for attr in endpoint_components:
            try:
                base = getattr(base, attr)
                assert base
            except Exception:
                raise AssertionError(f"Could not find a client endpoint for the {server_endpoint} server endpoint")
