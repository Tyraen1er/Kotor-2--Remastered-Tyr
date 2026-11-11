
void main()
{
	ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(3001), GetLocation(OBJECT_SELF));
	DestroyObject(OBJECT_SELF, 0.0, TRUE, 0.0, 0);
}