def CreateInferenceModifier(model_type, params=None, **kwargs):
    """
    Creates an inference modifier dictionary based on the model type and provided parameters.
    
    Parameters:
        model_type (str): The type of model ('claude', 'jurassic', or 'command').
        params (dict, optional): A dictionary of parameters. Defaults to None.
        **kwargs: Arbitrary keyword arguments.
        
    Returns:
        dict: A dictionary containing the inference modifier parameters for the specified model type.
    
    Raises:
        ValueError: If an unknown model_type is provided.
    """
    if params is None:
        params = kwargs
    
    if model_type == 'claude':
        return {
            "max_tokens_to_sample": params.get("max_tokens", 4096),
            "temperature": params.get("temperature", 0.5),
            "top_k": params.get("top_k", 250),
            "top_p": params.get("top_p", 1),
            "stop_sequences": params.get("stop_sequences", ["\n\nHuman"]),
        }
    elif model_type == 'jurassic':
        return {
            "temperature": params.get("temperature", 0.5),
            "topP": params.get("top_p", 1),
            "maxTokens": params.get("max_tokens", 4096),
            "stopSequences": params.get("stop_sequences", ["\n\nHuman"]),
        }
    elif model_type == 'command':
        return {
            "temperature": params.get("temperature", 0.5),
            "p": params.get("top_p", 1),
            "k": params.get("top_k", 250),
            "max_tokens": params.get("max_tokens", 4096),
            "stop_sequences": params.get("stop_sequences", ["\n\nHuman"]),
        }
    else:
        raise ValueError(f"Unknown model_type: {model_type}")
