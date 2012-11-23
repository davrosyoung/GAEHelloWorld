__author__ = 'dave'
import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()


        self.response.headers['Content-Type'] = 'text/html'
        self.response.write( '<html>' )
        self.response.write('<body>' )

        if user:
            self.response.write( 'Hello, ' + user.nickname() )
        else:
            self.redirect( users.create_login_url( self.request.uri ) )

#        self.response.write( 'Hello, webapp2 World!')
#        self.response.write( '<img src="images/PollyLogo.png">')
#        self.response.write( '</body>' )
#        self.response.write( '</html>' )


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)