from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:

    @staticmethod
    def split(text):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=600,
            chunk_overlap=100
        )

        return splitter.split_text(text)