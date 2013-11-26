create text search dictionary usspending ( template = simple, stopwords = US_Spending );
create text search configuration usspending ( copy = simple );
alter text search configuration usspending alter mapping for asciiword with usspending;
commit;
