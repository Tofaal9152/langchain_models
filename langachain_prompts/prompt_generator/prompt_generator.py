from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    name="Foods_Origin",
    validate_template=True,
    input_variables=["food_name", "language_name", "length"],
    template="""
        You are a helpful assistant that provides information about food.

        Food Name: {food_name} 
        Explanation Language: {language_name}  
        Explanation Length: {length}  

        Please include the following details:
        1. The color of the food  
        2. The origin of the food  
            """,
)

template.save("prompt_template/food.json")
