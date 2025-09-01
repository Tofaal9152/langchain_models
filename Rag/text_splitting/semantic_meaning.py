from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

text = """Apple Inc. is widely known for its iPhones and MacBooks, but in the world of agriculture, an apple is a fruit grown on trees and consumed worldwide. Apple farming involves selecting the right soil, providing irrigation, and protecting the trees from pests. Different varieties of apples include Fuji, Gala, Honeycrisp, and Granny Smith, each with unique flavor and texture.

Bannana 

lichu 
.

Mangoes are tropical fruits enjoyed for their sweet taste and juicy texture. Mango cultivation requires a warm climate and well-drained soil. Popular varieties include Alphonso, Kent, and Haden. Mangoes are often used in smoothies, desserts, and salads.

Grapes grow in clusters on vines and are used for eating fresh, making wine, and producing raisins. They require careful pruning and pest management. Common types are Concord, Thompson Seedless, and Red Globe.

Pineapples are tropical fruits with a spiky exterior and sweet, tangy flesh. They are grown in warm climates and need well-drained, sandy soil. Pineapples are rich in vitamin C and are used in juices, desserts, and savory dishes.
"""

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation"
)
chunks = text_splitter.create_documents([text])


print(len(chunks))
print((chunks))

# for i in chunks:
#     print(f"{i}\n")
