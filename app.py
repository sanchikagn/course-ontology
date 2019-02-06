from owlready2 import *

# onto_path.append("/home/kasumi/PycharmProjects/CourseOntology")
# course_ontology = get_ontology("/home/kasumi/PycharmProjects/CourseOntology/english.owl").load()
#
# print(course_ontology.base_iri)
# for lesson in course_ontology.classes():
#     print(lesson)


class Course(Thing):
    namespace = None

    def __init__(self):
        course_world = World()
        course_world.get_ontology("file://resources/english.owl").load()
        sync_reasoner(course_world)
        self.graph = course_world.as_rdflib_graph()

    def get_queried(self):
        query = "base <http://www.itfac.lk/kasumi/ontologies/english.owl> " \
                "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>" \
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>" \
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                "SELECT DISTINCT ?s ?p ?o " \
                "WHERE { " \
                "{?s ?p ?o}." \
                "}"

        query_2 = "base <http://www.itfac.lk/kasumi/ontologies/english.owl> " \
                  "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>" \
                  "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>" \
                  "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                  "SELECT ?p " \
                  "WHERE {" \
                  "{?s ?p ?o}." \
                  "}"

        results_list = self.graph.query(query_2)

        for item in results_list:
            print(item)


run_query = Course()
run_query.get_queried()
