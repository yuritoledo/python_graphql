import graphene

class User(graphene.ObjectType):
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(self, info):
        return User(name='Yuri', email='hahahaha')

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, name, email, password):
        user = User(name=name, email=email, password=password)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)