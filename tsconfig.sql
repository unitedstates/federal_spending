create text search dictionary federal_spending ( template = simple, stopwords = federal_spending );
create text search configuration federal_spending ( copy = simple );
alter text search configuration federal_spending alter mapping for asciiword with federal_spending;
commit;
