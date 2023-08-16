This project is to save some personal interested staff and want to learn things slowly. 


1. Store some iPython Notebook to do some interesting work. 
2. Store some Language Learning process. 
3. Each iPython Notebook Records one Function 

# LLAMA models 

$python3 convert.py --outfile models/13B/ggml-model-f16.bin --outtype f16 ../meta-models/llama-2-13b-chat


## Step 3: Convert the model to ggml format

$python convert-pth-to-ggml.py ../meta-models/llama-2-13b-chat 1

$ ./quantize ../meta-models/llama-2-13b-chat/ggml-model-f16.bin ./models/13B-chat/ggml-model-q4_0.bin 2


## Step 4: Run the model
$ ./main -m ./models/13B-chat/ggml-model-q4_0.bin \
        -t 8 \
        -n 128 \
        -p 'The first man on the moon was '