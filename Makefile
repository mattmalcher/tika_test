TRAINDIR=training

setup_env:
	python3 -m virtualenv env

setup_deps:
	pip3 install -r requirements.txt
	
activate:
	source env/bin/activate
	
train:
	python -m spacy init fill-config ./$(TRAINDIR)/base_config.cfg ./$(TRAINDIR)/config.cfg
	python -m spacy train \
	./$(TRAINDIR)/config.cfg \
	--paths.train ./$(TRAINDIR)/citation_labels_1.spacy \
	--paths.dev ./$(TRAINDIR)/citation_labels_1.spacy \
	--output ./$(TRAINDIR)/output


train_gpu:
	python -m spacy init fill-config ./$(TRAINDIR)/base_config.cfg ./$(TRAINDIR)/config.cfg
	python -m spacy train \
	./$(TRAINDIR)/config.cfg \
	--paths.train ./$(TRAINDIR)/citation_labels_1.spacy \
	--paths.dev ./$(TRAINDIR)/citation_labels_1.spacy \
	--output ./$(TRAINDIR)/output \
	--gpu-id 0