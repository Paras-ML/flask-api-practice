from flask import Flask,request

app = Flask(__name__)

#create the idea repository.This is where ideas will be stored

ideas = {

    1 : {

        "id":1,
        "idea_name":"ONDC",
        "idea_description":"Details about ONDC",
        "idea_author":"Adeeb"
    },
    2: {

        "id":2,
        "idea_name":"Save Soil",
        "idea_description":"Details about Saving Soils",
        "idea_author":"Ankit Sharma"
    }
}

'''
Create a Restful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    #Logic to fetch all the ideas
    return ideas 

'''
Create a Restful endpoint for creating a new idea
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #logic for creating a new idea
    try:


        #first read the request body
        request_body = request.get_json()


        #check if the idea id passed is not present already
        if request_body['id'] and request_body['id'] in ideas:

            return 'idea with the same id  already present',400


        #Insert the passed idea in the ideas dictionary
        ideas[request_body['id']] = request_body


        #return the response saying idea got saved
        return 'idea created and saved succefully',201
    except KeyError:
        return 'id is missing',400
    except:
        return 'some internal server error',500



if __name__ == '__main__':
    app.run(port=8080)
