from rest_framework import serializers

from core.models import Account, Invest


class AccountSerializer(serializers.ModelSerializer):
    assets = serializers.SerializerMethodField(method_name='get_assets', read_only=True)
    
    class Meta:
        model = Account
        fields = ['id', 'account_name','bank_name','account_number', 'assets']
        read_only_fields = ['id', 'account_name','bank_name','account_number','principal', 'assets']
        
    def get_assets(self, obj):
        '''총 자산 계산'''
        invests = Invest.objects.filter(account=obj.id)
    
        if invests.exists():
            assets = 0
            for invest in invests:
                assets += invest.holding_number * invest.holding.holding_price
            
            return assets
        
        return obj.principal

    
    
class AccountDetailSerializer(AccountSerializer):
    total_earnings = serializers.SerializerMethodField(method_name='get_total_earnings', read_only=True)
    earnings_rate = serializers.SerializerMethodField(method_name='get_earnings_rate', read_only=True)
    
    class Meta(AccountSerializer.Meta):
        fields = AccountSerializer.Meta.fields + ['principal', 'total_earnings', 'earnings_rate']
        
    def get_total_earnings(self, obj):
        '''총 수익금 계산'''
        total_earnings = self.get_assets(obj) - obj.principal
        return total_earnings
    
    def get_earnings_rate(self, obj):
        '''수익률 계산'''
        if obj.principal > 0:
            earnings_rate = self.get_total_earnings(obj) / obj.principal * 100
        earnings_rate = 'principal must be set'
        return earnings_rate
    