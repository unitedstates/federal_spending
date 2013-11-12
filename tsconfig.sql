create text search dictionary retinaburner ( template = simple, stopwords = retinaburner );
create text search configuration retinaburner ( copy = simple );
alter text search configuration retinaburner alter mapping for asciiword with retinaburner;
commit;