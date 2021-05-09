import cherrypy


class Client():
    #Définissons la route qui donne accès à des informations
    @cherrypy.expose
    @cherrypy.tools.json_in() 
    @cherrypy.tools.json_out()
    def 
