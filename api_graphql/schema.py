from graphql_auth import mutations
from .data.user.types import UsersNode
from graphene import relay, ObjectType, Schema, Field
from graphene_django.filter import DjangoFilterConnectionField
from .data.user.mutations import UpdateUsers
import graphql_jwt
from graphql_jwt.decorators import login_required
from users.models import ExtendUser
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery,ObjectType):
    #Consulas a la app Users
    allUsers = DjangoFilterConnectionField(UsersNode)
    #nodo
    user = relay.Node.Field(UsersNode)
    @login_required
    def resolve_allUsers(self, info, **kwargs):
        return ExtendUser.objects.all()
        #return Users.objects.filter(kwargs)
class AuthMutation(ObjectType):
    user_register  = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset = mutations.SendPasswordResetEmail.Field()

    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()

    #Cuando se olvido de la contraseña
    password_reset = mutations.PasswordReset.Field()
    #Cuando sabe la contraseña antigua
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()

class Mutation(AuthMutation,ObjectType):
    user_update = UpdateUsers.Field()